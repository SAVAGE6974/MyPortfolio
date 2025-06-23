document.addEventListener("DOMContentLoaded", function () {
    const loginBtn = document.getElementById("loginBtn");

    if (loginBtn) {
        loginBtn.addEventListener("click", function (event) {
            event.preventDefault(); // a 태그의 기본 이동 막기

            const left = window.screenX + 100;
            const top = window.screenY + 100;

            const loginPopup = window.open(
                "../html/login.html",    // 팝업으로 열 페이지 경로
                "로그인",                // 팝업 창 이름
                `width=500,height=600,left=${left},top=${top}` // 창 크기와 위치
            );

            // 팝업 차단되었을 경우 경고창 띄우기
            if (!loginPopup || loginPopup.closed || typeof loginPopup.closed === 'undefined') {
                alert("팝업이 차단되어 있습니다. 브라우저 설정에서 팝업을 허용해주세요.");
            }
        });
    }

    const signup = document.getElementById("signupBtn");

    if (signupBtn) {
        signupBtn.addEventListener("click", function (event) {
            event.preventDefault(); // a 태그의 기본 이동 막기

            const left = window.screenX + 100;
            const top = window.screenY + 100;

            const signupPopup = window.open(
                "../html/signup.html",    // 팝업으로 열 페이지 경로
                "회원가입",                // 팝업 창 이름
                `width=500,height=600,left=${left},top=${top}` // 창 크기와 위치
            );

            // 팝업 차단되었을 경우 경고창 띄우기
            if (!loginPopup || loginPopup.closed || typeof loginPopup.closed === 'undefined') {
                alert("팝업이 차단되어 있습니다. 브라우저 설정에서 팝업을 허용해주세요.");
            }
        });
    }
});
