# python-kanban



## 옛날에 정리한 동작들

보드를 만든다

Given
When 보드를 만들면
Then 보드가 생긴다

보드를 지운다

Given 보드가 이미 만들어 졌다면
When 보드를 지우면
Then 보드를 찾을 수 없다

보드를 지운다

Given 보드가 하나도 없다
When 보드를 지운다
Then 에러메세지가 나온다

카드을 추가한다

Given 보드가 있을 때
When TODO컬럼에 카드을 추가하면
Then 보드의 TODO컬럼에 카드이 추가된다

카드을 추가한다

Given 보드가 있을 때
When WIP컬럼에 카드을 추가하면
Then 보드의 WIP컬럼에 카드이 추가된다

카드을 추가한다

Given 보드가 있을 때
When Done컬럼에 카드을 추가하면
Then 보드의 DONE컬럼에 카드이 추가된다
