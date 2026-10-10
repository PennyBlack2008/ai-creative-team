# 15초 향수 광고 — 방향 승인부터 전달까지

설명용 예제입니다. 실제 서비스 대화 로그나 생성 영상이 아닙니다. 제품은 가상의 무상표 향수입니다.

## 1. 요청

```text
파란 유리 향수병의 15초 세로 광고 영상 프롬프트를 만들어줘.
9:16, 고급스럽고 차분하게, 자막·사람 없이. 콘셉트는 추천해줘.
```

## 2. 방향 확인

> 표준 작업입니다. 흰 스튜디오에서 파란 유리와 부드러운 빛을 강조하는 방향을 추천해요. 5초씩 3장면으로 구성하고 결과는 장면별 생성 프롬프트로 드리겠습니다. 이 방향으로 진행할까요?

이 응답에서는 제작을 시작하지 않습니다. 사용자: **“응, 그 방향으로. 프롬프트는 영어로.”**

## 3. 완성 예시

명세: 15초 편집 목표, 9:16, 흰 스튜디오, 무상표의 직사각형 코발트블루 유리병·평평한 은색 사각 캡, 차분한 제품 광고. 도구와 참조 이미지는 미지정입니다. 아래 시간은 최종 편집 길이이며 생성 도구의 지원 길이는 확인하지 않았습니다.

| 장면 | 시간 | 구도·동작 | 카메라 | 편집 |
|---|---|---|---|---|
| S1 | 0–5초, 5초 | 정면 미디엄, 병은 정지 | 느린 전진 | 시작/끝 안정 구간 확보 |
| S2 | 5–10초, 5초 | 병의 오른쪽 모서리 클로즈업, 정지 | 왼쪽에서 오른쪽으로 느린 이동 | 하드 컷 |
| S3 | 10–15초, 5초 | 중앙 전체 병, 정지 | 고정 | 마지막 1초 유지 |

**S1 — 복사할 문구**

```text
Vertical 9:16 product shot of one unbranded rectangular cobalt-blue glass perfume bottle with a flat square silver cap, centered on a matte white plinth in a white studio. The bottle stays still. Soft diffused light from camera left reveals the blue glass edges. Medium frontal framing, slow camera push-in, calm restrained mood. Keep the bottle geometry and cap unchanged. No people, lettering, or additional objects. Target edit duration: 5 seconds.
```

**S2 — 복사할 문구**

```text
Vertical 9:16 close-up of the right edge of one unbranded rectangular cobalt-blue glass perfume bottle with a flat square silver cap, on a matte white plinth in a white studio. The bottle stays still. Soft diffused light comes from camera left. The camera slides slowly from left to right, revealing the thickness of the blue glass. Keep the bottle geometry and cap unchanged. No people, lettering, or additional objects. Target edit duration: 5 seconds.
```

**S3 — 복사할 문구**

```text
Vertical 9:16 locked-off frontal product shot of one unbranded rectangular cobalt-blue glass perfume bottle with a flat square silver cap, centered on a matte white plinth in a white studio. Show the entire bottle with generous empty space above. The bottle stays still, softly lit from camera left, with subtle blue reflections on the plinth. Keep the bottle geometry and cap unchanged. No people, lettering, or additional objects. Hold a stable ending. Target edit duration: 5 seconds.
```

공통 유지: 같은 병·캡·광원·배경. 피해야 할 요소: 병 형태 변화, 캡 분리, 깜빡임, 글자, 사람. 별도의 negative prompt 옵션 지원은 확인하지 않았습니다. 참조 이미지가 있다면 같은 이미지를 각 장면에 적용할 수 있는지 생성 도구에서 확인하세요.

편집: 각 클립에서 안정적인 5초를 골라 연결합니다. 도구가 5초를 지원하지 않으면 지원 길이로 생성한 뒤 자릅니다. 음악은 별도로 선택해 편집하며 생성 도구의 음성 지원을 가정하지 않습니다. 비용이 드는 생성 호출은 이 예제에서 수행하지 않았습니다.

| 완료 기준 | 판정 | 근거 |
|---|---|---|
| R1 15초 구성 | 충족 | 5+5+5=15초, 구간 중복·누락 없음 |
| R2 세로형 9:16 | 충족 | 세 문구 모두 지정 |
| R3 사람·자막 제외 | 충족 | 세 문구와 공통 유지 조건 |
| R4 장면별 영어 프롬프트 | 충족 | S1–S3 |

프롬프트 작성·문구 검토 완료. 실제 영상의 형태 일관성, 화면비, 움직임, 최종 길이는 생성 후 확인해야 합니다.

상태: 전달 / 계획 v1 / 결과 v1 / 자동 수정 0/2 / 실제 영상 미검증.

## 실제 결과가 어긋나면

```text
S2에서 병이 둥글게 변했어. 나머지는 유지하고 그 장면만 고쳐줘.
```

AI는 이를 사용자 보고로 기록하고 참조 이미지 적용 가능 여부나 이동 폭 축소를 검토합니다. 보지 않은 영상을 직접 확인했다고 말하지 않습니다. 공통 수정 한도를 유지합니다.
