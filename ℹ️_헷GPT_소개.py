import streamlit as st

# 앱 소개 페이지
st.set_page_config(page_title="앱 소개", page_icon="ℹ️", layout="wide")

st.title("ℹ️ 헷GPT 소개")

st.markdown(
    """
    헷GPT: 실시간 코드 실행 및 미리보기 플랫폼
소개
헷GPT는 사용자가 직접 입력한 Python 및 HTML 코드를 웹 환경에서 실시간으로 실행하고, 그 결과를 즉시 확인할 수 있는 인터랙티브 플랫폼입니다. 이 애플리케이션은 개발자, 교육자, 학생 등 코딩 학습과 테스트를 필요로 하는 모든 이들에게 유용한 도구를 제공합니다.

주요 기능
Python 코드 실행: 사용자가 입력한 Python 코드를 서버 측에서 안전하게 실행하고, 그 결과를 출력합니다.
HTML 코드 미리보기: 입력된 HTML 코드를 렌더링하여 사용자가 작성한 웹 페이지를 실시간으로 미리보기할 수 있습니다.
에러 처리 및 디버깅 지원: 코드 실행 중 발생하는 오류를 상세하게 표시하여 사용자가 문제를 신속하게 파악하고 수정할 수 있도록 도와줍니다.
대화형 인터페이스: 직관적인 사용자 인터페이스를 통해 코드 입력과 결과 확인이 원활하게 이루어집니다.
기술 스택
프론트엔드: Streamlit을 활용하여 빠르고 효율적인 웹 인터페이스를 구축하였습니다.
백엔드: Python의 exec() 함수를 사용하여 코드 실행 기능을 구현하였으며, 표준 출력을 캡처하여 결과를 처리합니다.
보안: 코드 실행 시 발생할 수 있는 예외를 처리하고, 표준 출력을 제한하여 보안을 강화하였습니다.
사용 방법
코드 입력: 메인 페이지의 입력 창에 실행하고자 하는 Python 또는 HTML 코드를 입력합니다.
코드 실행: 입력을 완료하면 자동으로 코드가 실행되며, 결과가 화면에 표시됩니다.
결과 확인: 코드 실행 결과 또는 렌더링된 HTML 페이지를 실시간으로 확인할 수 있습니다.
개발 동기
코딩을 학습하거나 새로운 아이디어를 테스트할 때, 별도의 개발 환경을 설정하는 것은 번거로울 수 있습니다. 헷GPT는 이러한 불편을 해소하고자, 웹 브라우저만으로도 손쉽게 코드를 실행하고 결과를 확인할 수 있는 환경을 제공하기 위해 개발되었습니다.

향후 계획
다양한 언어 지원: 현재는 Python과 HTML만 지원하지만, JavaScript, CSS 등 다른 언어의 코드 실행 및 미리보기 기능을 추가할 예정입니다.
사용자 코드 저장: 사용자가 작성한 코드를 저장하고 관리할 수 있는 기능을 도입하여, 지속적인 학습과 개발에 도움이 되도록 할 계획입니다.
협업 기능: 여러 사용자가 동시에 코드를 작성하고 수정할 수 있는 실시간 협업 기능을 구현할 예정입니다.
    """,
    unsafe_allow_html=True
)