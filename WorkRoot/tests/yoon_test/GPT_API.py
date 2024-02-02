import openai
import time

# OpenAI API 키 설정
openai.api_key = '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' #moonsong Ai

def call_openai_api(_prompt):
    try:
        response = openai.Completion.create(
           engine="gpt-3.5-turbo-instruct",  # GPT-3.5의 최신 버전을 사용하세요.
            prompt=_prompt,  # 수정된 부분: prompt 매개변수에 _prompt 변수를 전달
            temperature=0.5,
            max_tokens=200,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        return response.choices[0].text.strip()
    except openai.error.RateLimitError as e:
        print("Rate limit exceeded. Waiting to retry...")
        # 필요에 따라 대기 시간을 조절하세요. 여기서는 1시간 대기합니다.
        # time.sleep(60 * 60)
        # 재시도
        # return call_openai_api(_prompt)

# 사용 예
text = """어 철수야 뭐 매장에 무슨 일 있어 그런 건 아니고요 어 그럼 무슨 일인데 야 뭔데 그렇게 우울증을 
해 빨리 말해 아하 다른게 아니라 월급날이 저희가 10일인데 지금 20일인데 월급이 안 들어와서요 아 그거 그냥 알잖아 
형이 요즘에 또 다른 매장 차린다고 지금 급하게 돈을 좀 쓰느라 그러지 너도 알잖아 아 아니 저번에도 그러시 다가 끝내요 뭐 
야 그건 내가 안 준게 아니라 네가 매장에서 물건 지나서 다 깨 먹어서 참치킨 거잖아 아 참 말 되게 서운하게 하네 아 그거 얼마도 안 됐는데 됐고
  아무튼 이번 기회는 이번 달하는 줄테니까 좀 참아라 너는 무슨 남자애가 참을성이 없냐 이해해 야 너 지금 한숨 쉬었어 야 알바생 님이 알바생 본문을 
  다 하라고 형 이 아련히 잘해 줄 때 잘 알아보고 야 지금 이거 알바 하려고 애들 주유소 있는 거 아니지요 야 그리고 너는 꼭 12시만 되면 꼭 뭘 처먹고 
  아주 손님들 거지같이 하더라 아 그건 휴게 시간이잖아요 야 더 뭐가 힘들다고 휴게실 바늘 갔냐 야 네가 아무튼이 똑바로 해라 안 그러면 또 차감 시킨다."""

#_prompt=f"다음 텍스트에서 법률적 쟁점이 될 만한 키워드를 단어로 내용만 출력 해주세요:\n'{text}'"
_prompt=f"다음 텍스트를 법적인 쟁점이 될만한 사실만 요약해서 내용만 출력 해주세요:\n'{text}'"

print(_prompt)
re_text = call_openai_api(_prompt)
print("="*40)
print(re_text)
