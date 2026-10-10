# AI Creative Team · 함께만들기

**한 번 붙여 넣고, 원하는 일을 말하세요. AI가 기획 → 제작 → 검토 → 전달을 맡습니다.**

영상·이미지 생성 프롬프트부터 문서, 조사, 실행 계획까지. 한국어를 기본으로 하는 일반인용 역할 기반 프롬프트 키트입니다. 설치, GitHub 가입, 코딩 지식, API 키가 필요 없습니다.

## 지금 사용하기

1. **[복사용 프롬프트 열기](https://raw.githubusercontent.com/PennyBlack2008/ai-creative-team/main/dist/ai-creative-team.txt)** → 전체 선택 → 복사합니다.
2. ChatGPT 또는 Claude의 새 대화에 붙여 넣고 보냅니다.
3. 아래처럼 원하는 일을 말합니다. 프롬프트 끝에 요청을 붙여 한 번에 보내도 됩니다.

```text
함께만들기: 파란 유리 향수병의 15초 세로 광고 영상 프롬프트를 만들어줘.
고급스럽고 차분하게, 자막 없이. 콘셉트는 추천해줘.
```

AI가 방향을 물으면 “그 방향으로 진행해줘”라고 답하면 됩니다. 바로 맡기고 싶으면 “네가 정해서 초안까지 완성해줘”라고 덧붙이세요. 명령어 이름을 외울 필요 없이 평소처럼 요청해도 됩니다.

원문 링크가 열리지 않으면 [저장소의 프롬프트 파일](dist/ai-creative-team.txt)을 여세요. 모든 전문 모듈이 포함되어 있어 추가 파일을 붙일 필요가 없습니다. 저장소 관리자는 이 텍스트를 메신저로 전달해도 됩니다.

> 이것은 하나의 AI가 역할을 순서대로 수행하도록 하는 **프롬프트**입니다. 실제 독립 에이전트, 앱 기능 설치, 자동 영상 생성, 대화 간 기억을 제공하지 않습니다. 도구 사용 가능 여부와 지시 준수는 사용 중인 서비스·모델에 따라 달라집니다. 특정 모델에서의 성능 보장은 하지 않습니다.

## 어떤 도움을 받나요?

| 원하는 일 | 받을 수 있는 결과 | 예제 |
|---|---|---|
| 영상 생성 | 제작 명세, 장면표, 장면별 복사용 문구, 편집·검수 지침 | [15초 제품 광고](examples/video.md) |
| 이미지 생성 | 구도·색·빛·유지 조건을 담은 프롬프트 | [포스터](examples/image.md) |
| 문서·발표 | 완성 본문 또는 슬라이드별 메시지 | [안내문](examples/document.md) |
| 조사 | 주장과 출처를 연결한 정리, 미확인 항목 | [자료 없는 최신 조사](examples/research.md) |
| 계획 | 일정·담당·선행 조건·완료 기준 | [작은 전시](examples/planning.md) |

텍스트만 가능한 채팅에서는 프롬프트나 본문을 전달합니다. 실제 파일이나 영상이 필요하면 그 도구와 결과물에 접근할 수 있어야 합니다. ‘프롬프트 검토 완료’와 ‘실제 영상 확인 완료’를 구분합니다.

## 작업에 맞게 가볍게

| 경로 | 예 | 기본 동작 |
|---|---|---|
| 간단 LIGHT | 생일 문구, 짧은 문장 수정 | 바로 만들고 확인 |
| 표준 STANDARD | 광고 프롬프트, 안내문 | 짧은 기획, 필요한 방향 결정, 제작·검토 |
| 복합 COMPLEX | 시리즈 캠페인, 여러 자료 조사 | 단계별 계획·제작과 통합 확인 |

기본은 자동입니다. “간단하게 해줘”, “정확성 위주로”, “창의적인 방향으로”처럼 바꿀 수 있습니다. 필수 조건을 생략하는 설정은 아닙니다. 결과를 크게 바꾸는 질문만 한 번에 최대 3개 합니다.

## AI 안에서 나뉘는 책임

| 역할 | 하는 일 |
|---|---|
| 총괄 Orchestrator | 범위·진행·승인·다음 행동 관리 |
| 기획자 Planner | 원하는 결과와 완료 기준 정리 |
| 제작자 Creator | 바로 쓸 수 있는 결과 제작 |
| 비평가 Critic | 조건 위반·모순 확인, 불필요한 것 덜어내기 |
| 검증자 Validator | 실제 확인한 증거로 완료 여부 판단 |

역할극 대화는 보여주지 않습니다. 검토자는 제작자의 설명보다 요청과 결과를 대조합니다. 같은 AI의 검토이므로 완전히 독립적인 검증은 아닙니다.

## 승인은 꼭 필요한 때만

- 아직 정하지 않은 중요한 방향은 먼저 묻습니다. 이미 지정했거나 맡긴 범위는 다시 묻지 않습니다.
- 최종 결과는 바로 보여줍니다. 게시·전송·결제 등 외부 실행은 구체적인 권한이 있어야 합니다.
- “네가 알아서 초안까지”는 게시 허가가 아닙니다. 이미 승인한 동일 실행은 재확인하지 않습니다.
- 자동 수정은 최초 초안 뒤 최대 2회입니다. 같은 필수 결함이 연속 두 번 남으면 더 일찍 멈춥니다. 원인과 다른 접근을 제시하며, 추가 작업은 새 수정 예산에 동의한 뒤 합니다.

“조명만 더 따뜻하게 해줘”처럼 수정할 부분을 말하세요. “마음에 안 들어”만으로 무엇이 문제인지 알기 어려우면 핵심 차이를 짧게 묻습니다. [수정·이어하기 예제](examples/rework-handoff.md)를 참고하세요.

## 대화를 옮길 때

“이어하기 카드 만들어줘”라고 요청하세요. 새 채팅에 **마스터 프롬프트 + 카드 + 필요한 결과물/첨부**를 붙여 넣으면 됩니다. 카드에는 목표, 승인된 조건, 현재 결과, 수정 횟수, 미확인 사항이 들어갑니다. 채팅 간 자동 저장은 없습니다. 새 대화의 외부 실행 권한은 직접 알려주세요.

## 신뢰 범위와 테스트

AI는 읽지 않은 출처나 보지 않은 영상을 검증했다고 말하지 않도록 지시받습니다. 이 규칙 자체가 모델의 오류를 차단하는 프로그램은 아닙니다. 최신 정보와 중요한 의사결정은 원자료를 확인하세요.

- 배포 파일 일치, 파일 누락, 문서 링크, 테스트 사례 구조는 자동 검사합니다.
- 승인 대기, 증거 한계, 수정 중단, 상태 복원은 [행동 평가 시나리오](tests/README.md)로 별도 평가합니다.
- 예제는 기대 동작을 설명하기 위해 작성한 샘플입니다. ChatGPT/Claude 실측 로그나 실제 영상 생성 결과가 아닙니다.
- 현재 검증 범위는 [검증 기록](docs/validation.md)에 공개합니다.

## 유지보수하는 분께

사용자는 이 부분을 건너뛰어도 됩니다. Python 3.10 이상, 외부 패키지 없이 실행합니다.

```sh
python3 scripts/build.py
python3 scripts/build.py --check
python3 -m unittest discover -s tests -v
```

`core/`는 공통 규칙, `roles/`는 역할 계약, `specialists/`는 분야별 기준입니다. `manifest.json` 순서대로 합쳐 `dist/ai-creative-team.txt`를 만듭니다. 배포 파일을 직접 고치지 마세요. [기여 방법](CONTRIBUTING.md) · [설계 배경](docs/design.md) · [변경 기록](CHANGELOG.md)

## 출발점

[solve-issue-team](https://github.com/PennyBlack2008/solve-issue-team)의 승인, 계획 대비 검토, 감산 리뷰, 반복 실패 중단, 상태 인계 접근을 비개발자용으로 재설계했습니다. 개발 전용 명령·Git 절차는 포함하지 않았습니다. [참고 기준과 출처](docs/design.md)에 확인한 원본 버전을 기록했습니다.

MIT License. 이 저장소의 새 문서·프롬프트·스크립트에 적용됩니다.

## English summary

A Korean-first, copy-and-paste workflow prompt for everyday creative work, documents, research, and planning. One assistant switches between orchestrator, planner, creator, critic, and validator responsibilities. Includes lightweight/standard/complex routing, scoped approvals, two automatic rework passes, evidence boundaries, portable state, and video/image specialists. No installation or API key is required to use the prompt. It is not an autonomous multi-agent runtime. Examples are illustrative; cross-product live evaluations are not yet recorded.
