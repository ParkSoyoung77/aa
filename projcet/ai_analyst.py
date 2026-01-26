import mysql.connector
from openai import OpenAI

# 1. 설정 (본인의 정보로 수정)
client = OpenAI(api_key="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") # GPT API 키

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1111",  # 이 부분이 app.py와 똑같이 "1111"인지 확인!
        database="quizdb",
        charset='utf8mb4'
    )

def ask_ai_analyst(user_question):
    prompt = f"""
    당신은 MariaDB 전문가입니다. 아래 실구조 스키마를 참고하여 SQL 쿼리만 작성하세요.
    
    [실제 테이블 스키마 정보]
    1. Quiz_Bank
       - 컬럼: quiz_id(PK), question, option_1, option_2, option_3, option_4, answer_idx, category, difficulty
    2. Quiz_Results
       - 컬럼: result_id(PK), user_name, quiz_id(FK), is_correct, solved_at
    
    질문: "{user_question}"
    
    [작성 규칙]
    1. 반드시 'Quiz_Bank.quiz_id = Quiz_Results.quiz_id'를 사용하여 JOIN 하세요.
    2. Quiz_Bank에는 'id'라는 컬럼이 없으므로 반드시 'quiz_id'를 사용하세요.
    3. 오직 SELECT 쿼리만, 마크다운 없이 문장만 출력하세요.
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    
    # [수정 포인트] GPT 응답에서 불필요한 공백 및 마크다운 제거
    sql = response.choices[0].message.content.strip()
    sql = sql.replace("```sql", "").replace("```", "").strip()
    
    # 보안 검증: 대소문자 구분 없이 SELECT로 시작하는지 확인
    if not sql.upper().startswith("SELECT"):
        return f"보안 위반: 생성된 문장이 조회가 아닙니다 -> ({sql})", None

    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        return sql, results
    except Exception as e:
        return sql, f"쿼리 실행 에러: {str(e)}"
    finally:
        conn.close()

if __name__ == "__main__":
    print("=== AI SQL Analyst 가동 (보안 강화 버전) ===")
    while True:
        q = input("\n분석 질문 입력 (종료: q): ")
        if q.lower() == 'q': break
        
        sql, data = ask_ai_analyst(q)
        print(f"\n[생성된 SQL]\n{sql}")
        print(f"\n[분석 결과]")
        if isinstance(data, list):
            for row in data: print(row)
        else:
            print(data)