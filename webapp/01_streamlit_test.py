# bash : streamlit run 01_streamlit_test.py --server.port 8051
import streamlit as st
from langchain_core.messages import ChatMessage

class ChatWeb:
    def __init__(self, page_title="Gazzi Chatbot", page_icon=":books:"):
        # 페이지 제목과 아이콘 설정
        self._page_title = page_title
        self._page_icon = page_icon

    def print_messages(self):
        """세션에 저장된 이전 대화 기록을 출력합니다."""
        if "messages" in st.session_state and len(st.session_state["messages"]) > 0:
            for chat_message in st.session_state["messages"]:
                st.chat_message(chat_message.role).write(chat_message.content)

    def run(self):
        """챗봇 앱 실행 함수."""
        # 웹 페이지 기본 환경 설정
        st.set_page_config(
            page_title=self._page_title,
            page_icon=self._page_icon
        )
        st.title(self._page_title)

        # 대화 기록 목록 초기화
        if "messages" not in st.session_state:
            st.session_state["messages"] = []

        # 이전 대화 기록 출력
        self.print_messages()

        # 사용자 입력을 받기
        if user_input := st.chat_input("질문을 입력해 주세요."):
            # 사용자가 입력한 내용 출력 및 저장
            st.chat_message("user").write(user_input)
            st.session_state["messages"].append(ChatMessage(role="user", content=user_input))

            # AI의 답변 생성 및 출력
            with st.chat_message("assistant"):
                msg_assistant = f"당신이 입력한 내용: {user_input}"
                st.write(msg_assistant)
                st.session_state["messages"].append(ChatMessage(role="assistant", content=msg_assistant))


if __name__ == '__main__':
    web = ChatWeb()
    web.run()
