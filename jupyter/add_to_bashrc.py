import os

def add_to_bashrc():
    # .bashrc에 추가할 bash 코드
    bash_snippet = """
# Jupyter in tmux auto-start function
start_jupyter_tmux() {
    # 1. 기준이 될 폴더 경로 설정 (실제 경로에 맞게 수정하세요)
    # 예: ~/storage/downloads/github 또는 ~/github
    TARGET_DIR="$HOME/github"

    # 폴더가 없는 경우를 대비해 체크
    if [ ! -d "$TARGET_DIR" ]; then
        echo "Error: $TARGET_DIR 폴더가 존재하지 않습니다."
        return
    fi

    # 2. tmux 세션 생성 시 --notebook-dir 옵션 추가
    tmux new-session -d -s jupyter "jupyter notebook --notebook-dir=$TARGET_DIR --NotebookApp.token='' --NotebookApp.password=''"

    echo "Jupyter started at: $TARGET_DIR"

    # 3. 종료 시 자동 정리
    trap "tmux kill-session -t jupyter; exit" EXIT
}

start_jupyter_tmux
"""

    # .bashrc 파일 경로 설정
    bashrc_path = os.path.expanduser("~/.bashrc")

    # 이미 코드가 존재하는지 확인
    if os.path.exists(bashrc_path):
        with open(bashrc_path, "r", encoding="utf-8") as file:
            content = file.read()
            if "start_jupyter_tmux()" in content:
                print("⚠️ 이미 .bashrc에 'start_jupyter_tmux' 함수가 존재합니다. 추가하지 않고 종료합니다.")
                return

    # .bashrc 파일에 코드 추가 (append 모드)
    with open(bashrc_path, "a", encoding="utf-8") as file:
        file.write("\n" + bash_snippet)

    print("✅ 성공적으로 .bashrc에 코드를 추가했습니다.")
    print("터미널에 다음 명령어를 입력하여 변경 사항을 즉시 적용하세요:")
    print("source ~/.bashrc")

if __name__ == "__main__":
    add_to_bashrc()
