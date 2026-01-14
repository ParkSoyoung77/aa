from flask import Flask, render_template_string
import pyautogui

app = Flask(__name__)

# 핸드폰에 보여줄 PPT 리모컨 화면 (HTML)
html_code = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PPT 리모컨</title>
    <style>
        body { text-align: center; font-family: sans-serif; background-color: #222; color: white; padding-top: 50px; }
        .btn-container { display: flex; flex-direction: column; align-items: center; }
        button { width: 80%; height: 120px; font-size: 30px; margin: 15px; border-radius: 20px; border: none; cursor: pointer; font-weight: bold; }
        .next { background: #28a745; color: white; }
        .prev { background: #ffc107; color: black; }
        .f5 { background: #007bff; color: white; height: 70px; font-size: 20px; }
    </style>
</head>
<body>
    <h1>PPT Remote Control</h1>
    <div class="btn-container">
        <button class="f5" onclick="fetch('/start')">슬라이드 쇼 시작 (F5)</button>
        <button class="next" onclick="fetch('/next')">다음 슬라이드 ▶</button>
        <button class="prev" onclick="fetch('/prev')">이전 슬라이드 ◀</button>
        <button class="f5" style="background:#6c757d;" onclick="fetch('/esc')">쇼 종료 (ESC)</button>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html_code)

@app.route('/next')
def next_slide():
    pyautogui.press('right') # 오른쪽 화살표 키 입력
    return "Next"

@app.route('/prev')
def prev_slide():
    pyautogui.press('left') # 왼쪽 화살표 키 입력
    return "Prev"

@app.route('/start')
def start_show():
    pyautogui.press('f5') # F5 키 입력
    return "Start"

@app.route('/esc')
def stop_show():
    pyautogui.press('esc') # ESC 키 입력
    return "Stop"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)