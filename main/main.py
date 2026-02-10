<!doctype html>
<html>
    <head>
        <meta charset="UTF-8" />
        <title>타자기 효과</title>
    </head>
    <body>
        <h1>타자기 효과 실습</h1>
        <input id="msg" placeholder="메시지를 입력하세요..." />
        <p id="status"></p>

        <script>
            let ws = new WebSocket("ws://127.0.0.1:5000/ws");

            let typingTimer; // 타이핑 멈춤 감지용 타이머
            const typingTimeout = 1000; // 1초 뒤 "stop" 전송

            document.getElementById("msg").addEventListener("input", () => {
                ws.send("typing"); // 타이핑 시작 이벤트 전송

                clearTimeout(typingTimer);
                typingTimer = setTimeout(() => {
                    ws.send("stop"); // 입력 멈추면 stop 이벤트 전송
                }, typingTimeout);
            });

            ws.onmessage = (event) => {
                document.getElementById("status").innerText = event.data;
            };
        </script>
    </body>
</html>
        data = ws.receive()
        if data is None:
            break
    conn.remove(ws)

def background_job():
    while True:
        time.sleep(5)
        for ws in list(conn):
            ws.send("5초마다 알림 발송 중")

threading.Thread(target=background_job, daemon=True).start()

if __name__ == "__main__":
    app.run(debug=True)