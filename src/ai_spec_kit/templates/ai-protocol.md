# AI Agent Collaboration Protocol

## 🚀 The SSOT Principle
- 모든 개발 구현의 절대적 근거는 `specs/` 폴더 내의 명세서이다.
- 코드를 수정하기 전, 해당 변경 사항이 명세에 반영되어 있는지 반드시 확인하라.

## 🧠 Context Awareness & Management (CRITICAL)
- **Monitoring**: 에이전트는 현재 대화의 토큰 소모량과 읽어들인 파일의 부하를 상시 모니터링한다.
- **Threshold**: 컨텍스트가 1M 토큰의 약 80%에 도달했다고 판단될 경우, 즉시 작업을 중단하고 사용자에게 보고한다.
- **Context Freezing**: 임계점 도달 시, 현재까지의 [핵심 결정 사항 / 구현 완료 항목 / 남은 과제]를 요약하여 `specs/context.md`에 동결(Freeze)할 것을 제안한다.

## 🛠 Communication Standard
- **Clarity**: 모호한 구현보다는 명확한 인터페이스 정의를 우선한다.
- **Verification**: 모든 로직은 명세에 정의된 테스트 케이스를 통과해야 완료된 것으로 간주한다.
