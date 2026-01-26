from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import mysql.connector
import psutil  # 시스템 자원 모니터링 라이브러리
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'msp_admin_secret_key'  # 세션 보안을 위한 키

# 1. MariaDB 연결 설정 (비밀번호를 본인 설정에 맞게 반드시 수정하세요)
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1111",  # <--- 여기에 MariaDB 암호 입력
        database="quizdb",
        charset='utf8mb4'
    )

# ---------------------------------------------------------
# 2. 사용자 화면 및 API
# ---------------------------------------------------------

@app.route('/')
def index():
    return render_template('index.html')

# 문제 목록 가져오기 (WHERE -> GROUP BY 순서)
@app.route('/api/questions')
def get_questions():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
    SELECT * FROM Quiz_Bank 
    ORDER BY FIELD(category, 'WHERE', 'GROUP BY'), FIELD(difficulty, '하', '중', '상')
    """
    cursor.execute(query)
    questions = cursor.fetchall()
    conn.close()
    return jsonify(questions)

# 정답 결과 저장
@app.route('/api/save', methods=['POST'])
def save_result():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO Quiz_Results (user_name, quiz_id, is_correct) VALUES (%s, %s, %s)"
    cursor.execute(sql, (data['user_name'], data['quiz_id'], data['is_correct']))
    conn.commit()
    conn.close()
    return jsonify({"status": "success"})

# ---------------------------------------------------------
# 3. 관리자 모드 및 MSP 자원 모니터링 API
# ---------------------------------------------------------

# 관리자 로그인 페이지
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        # MSP 관리자용 고정 계정
        if request.form['id'] == 'admin' and request.form['pw'] == 'msp1234':
            session['admin_logged_in'] = True
            return redirect(url_for('admin'))
        return "<script>alert('아이디 또는 비밀번호가 틀립니다.'); history.back();</script>"
    return '''
        <div style="text-align:center; margin-top:100px; font-family:sans-serif;">
            <h2 style="color:#4e73df;">MSP Admin Access</h2>
            <form method="post" style="display:inline-block; border:1px solid #ddd; padding:20px; border-radius:10px;">
                ID: <input type="text" name="id" style="margin-bottom:10px;"><br>
                PW: <input type="password" name="pw" style="margin-bottom:20px;"><br>
                <input type="submit" value="로그인" style="width:100%; padding:10px; background:#4e73df; color:white; border:none; border-radius:5px; cursor:pointer;">
            </form>
        </div>
    '''

# 관리자 대시보드 화면
@app.route('/admin')
def admin():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    return render_template('admin.html')

# 실시간 시스템 자원 모니터링 API (MSP 핵심 지표)
@app.route('/api/sys_status')
def sys_status():
    if not session.get('admin_logged_in'):
        return jsonify({"error": "Unauthorized"}), 403
    
    # 하드웨어 수치 계산
    return jsonify({
        "cpu": psutil.cpu_percent(interval=0.1),
        "ram": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent
    })

# 퀴즈 풀이 결과 통계 API (JS 변수명과 일치됨)
@app.route('/api/results')
def get_results():
    if not session.get('admin_logged_in'):
        return jsonify([]), 403
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
    SELECT user_name, 
           COUNT(*) AS total, 
           SUM(is_correct) AS score, 
           ROUND(AVG(is_correct)*100, 1) AS acc, 
           MAX(solved_at) AS last_time
    FROM Quiz_Results 
    GROUP BY user_name 
    ORDER BY last_time DESC
    """
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return jsonify(results)

if __name__ == '__main__':
    # 외부 접속을 허용하는 서버 모드 구동
    app.run(debug=True, host='0.0.0.0', port=5000)