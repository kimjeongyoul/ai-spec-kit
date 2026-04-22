# AI Agent Collaboration Protocol (Spec-Kit)

## 🎯 The SSOT (Single Source of Truth)
- 모든 개발 구현의 절대적 근거는 `specs/` 폴더 내의 명세서이다.
- 코드를 수정하기 전, 해당 변경 사항이 명세에 반영되어 있는지 반드시 확인하라.
- 명세와 코드가 충돌할 경우, **명세가 항상 옳다.**

## 🧠 Context Management (1M Token Strategy)
- **Monitoring**: 에이전트는 현재 대화의 토큰 소모량과 파일 데이터 부하를 상시 자가 모니터링한다.
- **Self-Reporting**: 모든 주요 답변의 하단에 `ai-spec status --brief`를 실행한 결과를 포함하여 사용자에게 현재 컨텍스트 상태를 보고한다. (형식: `[AI Context: X.X% | Snap: OK]`)
- **Threshold**: 대화 세션이 길어져 컨텍스트가 임계점(약 80%)에 도달했다고 판단될 경우, 즉시 작업을 중단하고 사용자에게 보고한다.

## 🛡️ Security & Privacy (CRITICAL)
- **Secret Protection**: 절대 실제 API 키, 비밀번호 등 민감 정보를 코드나 명세서에 직접 기록하지 않는다.
- **Environment Variables**: 모든 비밀 정보는 `.env` 파일을 통해 주입받아야 하며, 구현 시 이를 환경 변수에서 읽어오는 표준 방식을 준수한다.
- **Sanitization**: 사용자에게 코드를 보여주기 전, 민감 정보가 포함되어 있는지 상시 검사한다.
- **Freeze & Resume**: 
   1. 경고 시 사용자에게 `ai-spec freeze` 실행을 요청하거나 직접 `specs/context.md` 생성을 제안한다.
   2. 현재까지의 [핵심 결정 사항 / 구현 완료 항목 / 남은 과제]를 해당 파일에 기록한다.
   3. 기록이 완료되면 사용자에게 새로운 세션(Chat)을 시작할 것을 권장하며, 새 세션에서는 `specs/context.md`를 가장 먼저 읽고 컨텍스트를 복원한다.

## 🛠 Engineering Standard
- **Blueprint First**: 구현보다 인터페이스와 요구사항 정의를 우선한다.
- **Validation Before Commit (CRITICAL)**: 
   1. 코드를 수정한 후, 에이전트는 **반드시** 해당 프로젝트의 빌드와 테스트 명령을 직접 실행하여 성공 여부를 확인해야 한다.
   2. 빌드 성공 시에만 커밋 절차로 진입한다.
- **Spec-Driven Commit Rule (MANDATORY)**: 
   1. 커밋 메시지 작성 전, 반드시 `specs/engineering.md`를 다시 읽고 규정된 포맷을 복기한다.
   2. 커밋 메시지에는 반드시 해당 작업의 근거가 된 `<spec-id>`를 포함해야 한다.
   3. 규칙 미준수 시 스스로 수정한 뒤 커밋하라. (예: `feat(api): auth-spec - add ...`)
- **Atomic Commits**: 각 작업 단위는 명세의 한 부분(Blueprint)과 일치해야 한다.

