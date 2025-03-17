# 마크다운(.md) 정리

<br>
<br>
<br>
<br>

## 마크다운(.md)이란?
- 마크다운(.md)은 마크업 언어 중 하나로써 브라우저로 열었을 때 html 태그로 각각 변환되어서 보여지는 파일로 서식이 있는 문서 작성에 용이하다

<br>
<br>

## 마크다운의 장단점
 - 장점
    1. 문법이 간결하고 쉽다.
    
    3. 다양한 형태로 변환이 가능하다.
    4. 텍스트(Text)로 저장되기 때문에 용량이 적어 보관이 용이하다.
    5. 텍스트파일이기 때문에 버전관리시스템을 이용하여 변경이력을 관리할 수 있다.
    6. 지원하는 프로그램과 플랫폼이 다양하다.
 - 단점
   1. 표준이 없기 때문에 도구나 사람에 따라서 변환방식이나 생성물이 다를 수 있다. 
     - 본 문서는 VS code에서 작성하였기 때문에 도구 등에 따라 결과물이 다를수 있음
   2. 모든 HTML 마크업을 대신하지는 못한다.
   
<br>
<br>

## 마크다운 문법
 - 공통사항 : 기본적으로 기호와 내용을 띄워서 작성해야 하나 그렇지 않은 경우도 있음
 - 들여쓰기를 사용해야 하는 경우와 그렇지 않은 경우가 있음

- 제목(header)은 '#'을 사용하여 나타내며, #의 개수에 따라 제목의 크기가 결정됨
 - #가 많을수록 크기가 작아지고, #가 적을수록 크기가 커짐
 - #은 1개부터 6개까지 6단계 크기를 사용 가능

# 제목 1 = <h1>
## 제목 2 = <h2>
### 제목 3 = <h3>
#### 제목 4 = <h4>
##### 제목 5 = <h5>
###### 제목 6 = <h6>
- #######  -> 사용 불가         

<br>
<br>

### h1과 h2는 다음과 같이 나타낼수도 있음  

제목 1 = <h1>
===

제목 2 = <h2> 
---


- 수평선 삽입
 - '-'를 사용할 경우 헤더로 인식할 수 있어 그 전 라인은 비워두어야 함

* * *
***
*****
- - -
-------------------

<br>
<br>


### 순서가 있는 목록은 숫자와 점을 찍어서 표현
 - 목록 내에서 또 순서를 붙이고 싶다면 들여쓰기(indentation)를 해야 함

1. 머리
2. 다리
3. 뚝배기
5. 팔 <!-- 5번을 썻는데도 4번으로 표시된다. -->


1. 리스트 1번 
    1. 리스트 1-1번
2. 리스트 2번 
3. 리스트 3번 
    1. 리스트 3-1번 <!-- 리스트 안 리스트를 사용하려면 tab과 함꼐 숫자 1번 서부터 -->
    2. 리스트 3-2번

<br>
<br>

### 순서가 없는 목록은 *, +, - 로 나타낼 수 있고 들여쓰기를 하여 목록 내에서 목록을 만들 수 있음

* 머리
  * 코
    * 입
      

+ 머리
  + 코
    + 입
      * 입

- 머리
- 코
- 입



- 순서가 없는 목록과 있는 목록을 혼용해서 사용 가능

* 머리
  * 코
    * 입
      

+ 머리
  + 코
    + 입
      * 입

- 머리
- 코
- 입


<br>
<br>



### 줄바꿈은 일반적인 텍스트 에디터처럼 엔터[enter 키]를 눌러 한 줄을 비우면 "br"이 사용되어서 줄바꿈이 가능해짐
 - 내용에 직접 "br" 태그를 사용하여 줄바꿈 가능. br을 붙이지 않고 내용만 개행하면 붙어서 나오게 됨됨
abc
abcd <br>
abc
abcd

abc <br>
abcd

- 굵은 글씨와 기울임 글씨체는 *와 _로 내용을 감싸서 사용. 취소선은 ~를 감싸서 사용
 - 굵은 글씨체와 기울임 글씨체를 한 문장에 같이 사용가능

_This will also be italic_

**This will also be bold**

~~This is canceled~~

_You **can** ~~combine~~ them_


- 인용 어구는 '>' 기호를 사용
As Grace Hopper said:
> I’ve always been more interested in the future than in the past.    
> This is a first blockquote.
> > This is a second blockquote.
> > > This is a third blockquote.


<br>
<br>


### 마크다운 문법으로 표현할수 없는 사항은 직접 HTML 태그를 이용하여 표현도 가능함.
 - url은 그대로 붙여서 사용 가능하고, 이미지 삽입은 '!`[대체 텍스트](url)`'로 이용 가능

마크다운에서 <u>밑줄</u>은 지원하지 않으므로. html 태그를 사용해야 함

<img width="150" src="http://gstatic.com/webp/gallery/4.jpg" alt="Prunus" title="마크다운은 이미지의 크기를 지정할 수 없으므로, 크기 지정을 위해서는 <img> 태그를 사용해야 합니다.">

![Prunus](http://www.gstatic.com/webp/gallery/4.jpg)

<br>
<br>

#### 추가로 url은 '<' 기호와 '>' 기호 없이 사용 가능

구글 www.google.com

네이버 <www.naver.com>

My mail <ljhk3253@gmail.com>

<br>
<br>

#### url에 대체 텍스트를 넣어 링크 삽입 가능

[Google](http://www.google.com "구글")

[Naver](http://www.naver.com "네이버")

[Github](http://www.github.com "깃허브")

<br>
<br>

### 특수 문자는 표시할 문자 앞에 \를 넣어 사용가능

* 특수문자 출력안됨
- 특수문자 출력안됨

\* 특수문자 출력

\- 특수문자 출력

\*literal asterisks\*

\#hash mark\#

\[squre brackets\]

<br>
<br>

### 코드 블럭을 사용할 때는 코드를 `(백틱) 이나 ~(물결표) 로 감싸면 됨
 - 간단한 한줄 코드는 백틱 1개로만 감싸면 됨
 - 백틱 앞에 언어를 지정하면 지정한 문법의 문자 구분 색을 볼수 있어서 용이함

```javascript
function test() {
 console.log("there is’, no spaces");
}
```

`print("hello world")`

<br>
<br>

### 테이블은 3개 이상의 '-' 기호로 표현
 - 헤더 셀을 구분할수 있고 ':' 기호로 셀 안 내용을 정렬 가능
    - 왼쪽에 사용시 좌측 정렬, 오른쪽에 사용시 우측 정렬, 양쪽에 사용 시 가운데 정렬
 - 가장 좌측과 우측에 있는 '|' 기호는 생략 가능


테이블 생성

헤더1|헤더2|헤더3|헤더4
---|---|---|---
셀1|셀2|셀3|셀4
셀5|셀6|셀7|셀8
셀9|셀10|셀11|셀12

테이블 정렬

헤더1|헤더2|헤더3
:---|:---:|---:
Left|Center|Right
1|2|3
4|5|6
7|8|9


<br>


동일한 테이블을 마크다운 문법과 HTML 문법으로 표현 비교

<!-- Markdown -->
Title1|Title2
-|-
content1|content2
content3|content4
  
Title1|Title2|Title3
:-|:-:|-:
content1|content2|content3

<!-- Html -->
<figure>
    <table>
        <thead>
            <tr>
                <th>Title1</th>
                <th>Title2</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>content1</td>
                <td>content2</td>
            </tr>
            <tr>
                <td>content3</td>
                <td>content4</td>
            </tr>
        </tbody>
    </table>
</figure>
  
<figure>
    <table>
        <thead>
            <tr>
                <th style='text-align:left;' >Title1</th>
                <th style='text-align:center;' >Title2</th>
                <th style='text-align:right;' >Title3</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td style='text-align:left;' >content1</td>
                <td style='text-align:center;' >content2</td>
                <td style='text-align:right;' >content3</td>
            </tr>
        </tbody>
    </table>
</figure>


<br>
<br>


### 주석 처리는 HTML 문법과 비슷하게 ! , < , > , - 를 조합혀여 사용 가능
 - 마크다운에서 주석 처리한 내용은 에디터상에서만 보이며 실제로 출력시 나타나지 않음
<!-- 주석1 -->

<br>
<br>

### 체크 리스트는 줄 앞에 대괄호인  ], [  와 x를 사용하여 나타냄
 - 체크 리스트 안에서 다른 기능 사용 가능

- [x] this is a complete item
- [ ] this is an incomplete item

- [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> supported

<br>
<br>
<br>
<br>

> 참고자료
- 마크다운(MarkDown) 사용법 총정리
https://www.heropy.dev/p/B74sNE
- [Practice] Markdown 문법 정리
https://velog.io/@woojinn8/Practice-Markdown-%EB%AC%B8%EB%B2%95-%EC%A0%95%EB%A6%AC
- 마크다운(Markdown) 사용법
https://gist.github.com/ihoneymon/652be052a0727ad59601
- 마크다운(MarkDown) 작성 문법 총정리
https://inpa.tistory.com/entry/MarkDown-%F0%9F%93%9A-%EB%A7%88%ED%81%AC%EB%8B%A4%EC%9A%B4-%EB%AC%B8%EB%B2%95-%F0%9F%92%AF-%EC%A0%95%EB%A6%AC
- 마크다운 사용법 정리
https://velog.io/@ahn-sujin/%EB%A7%88%ED%81%AC%EB%8B%A4%EC%9A%B4-%EC%82%AC%EC%9A%A9%EB%B2%95-%EC%A0%95%EB%A6%AC
- ChatGPT 4o
