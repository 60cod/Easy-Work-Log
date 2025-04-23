<!-- Language Selection Tabs -->
<p align="right">
  <a href="#readme-en">English</a> | <a href="#readme-ko">한국어</a>
</p>

---

<a id="readme-en"></a>
# Easy Work Log

Automatic Work Log Application

---

## Overview

Easy Work Log is a lightweight Windows application that automatically runs at a scheduled time, allowing you to write work logs with minimal user input. It uses a secure local LLM to generate natural language summaries and saves them as Google Docs on your Google Drive.

---

## Key Features

- Automatic launch and shutdown via Windows Task Scheduler (17:00/18:00)
- Web-based template page (Flask): work log input & one-click submission
- Local LLM for automatic work log generation
- Google Drive API integration: automatic creation and saving of Google Docs
- Logging and retry logic for error handling
- Lightweight and easy installation

---

## Installation & Usage

1. **Install Python 3.10+ and create a venv**
2. **Install required packages**
   ```bash
   pip install flask google-auth google-api-python-client
   ```
3. **Install llama.cpp (or Ollama) and prepare a model (EXAONE-3.5-2.4B-Instruct)**
4. **Prepare Google API credentials (`credential.json`) and complete OAuth2 authentication**
5. **Register app launch/exit schedule with Windows Task Scheduler**
6. **Run the app**
   ```bash
   python app.py
   ```
7. **Access the work log page in your browser (default: http://localhost:5959)**

---

## Example Folder Structure

```
Easy-Work-Log/
├── app.py
├── templates/
│   └── log_template.html
├── static/
├── llama_cpp/ (or ollama/)
├── credentials.json
├── token.json
├── config.yaml
├── development-checklist.md
├── application-design-docs.md
└── README.md
```

---

## Tech Stack
- Python 3.10+
- Flask
- llama.cpp (or Ollama)
- Google API (Drive, Docs)
- Windows Task Scheduler

---

## Development & Operation Checklist
- See [development-checklist.md](./development-checklist.md)

---

## Reference & Extension Ideas
- Multiple work log templates by type
- Slack/Webhook notification integration
- Log aggregation (DB or ELK)
- Unit tests (pytest)
- Work time tracking and visualization
- Monthly performance summary reports


---

<a id="readme-ko"></a>
# Easy Work Log

자동 업무 일지 작성 애플리케이션

---

## 개요

Easy Work Log는 매일 정해진 시각에 자동으로 실행되어 최소한의 사용자 입력으로 업무 일지를 작성할 수 있게 합니다. 보안 이슈 없는 로컬 LLM을 이용하여 자연스러운 문장으로 가공하고 Google Drive에 Docs 문서로 저장합니다.

---

## 주요 기능

- Windows Task Scheduler를 통한 자동 실행/종료 (17:00/18:00)
- Flask 기반 웹 템플릿 페이지(업무일지 입력, 작성 버튼)
- 로컬 LLM 으로 업무일지 자동 가공
- Google Drive API를 통한 Google Docs 문서 자동 생성 및 저장
- 오류/예외 발생 시 로깅 및 재시도
- 간편한 설치 및 경량화

---

## 설치 및 실행 방법

1. **Python 3.10+ 및 venv 가상환경 설치**
2. **필수 패키지 설치**
   ```bash
   pip install flask google-auth google-api-python-client
   ```
3. **llama.cpp(또는 Ollama) 설치 및 모델 (EXAONE-3.5-2.4B-Instruct) 준비**
4. **Google API 자격증명(credential.json) 준비 및 OAuth2 인증**
5. **Windows Task Scheduler에 앱 실행/종료 스케줄 등록**
6. **앱 실행**
   ```bash
   python app.py
   ```
7. **웹 브라우저에서 업무일지 작성(기본: http://localhost:5959)**

---

## 폴더 구조 예시

```
Easy-Work-Log/
├── app.py
├── templates/
│   └── log_template.html
├── static/
├── llama_cpp/ (또는 ollama/)
├── credentials.json
├── token.json
├── config.yaml
├── development-checklist.md
├── application-design-docs.md
└── README.md
```

---

## 기술 스택
- Python 3.10+
- Flask
- llama.cpp (또는 Ollama)
- Google API (Drive, Docs)
- Windows Task Scheduler

---

## 개발/운영 체크리스트
- [development-checklist.md](./development-checklist.md) 파일 참고

---

## 참고 및 확장 아이디어
- 업무유형별 템플릿 다중 선택 지원
- Slack/Webhook 알림 연동
- 로그 집계(DB 또는 ELK)
- 단위 테스트(pytest)
- 업무 시간 기록
- 그래프 제공
- 월별 업무 성과 요약
