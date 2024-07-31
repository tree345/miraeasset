def ask_investment_experience():
    print("투자 경험이 있으신가요?:")
    print("1. 처음이에요")
    print("2. 해본 경험이 있어요")

    choice = input("번호를 입력하세요 (1, 2 중에서 하나 골라주세요): ")

    selections = []

    if choice == '1':
        while True:
            print("\n투자에 대해서 잘 아십니까?")
            print("1. 전혀 모름")
            print("2. 기본 지식 있음")
            print("3. 투자에 대해 잘 알고 있음")

            knowledge_choice = input("번호를 입력하세요 (1, 2, 3 중에서 하나 골라주세요): ")
            if knowledge_choice in ['1', '2', '3']:
                selections.append(knowledge_choice)
                break
            else:
                print("잘못된 입력입니다. 1, 2, 3 중에서 하나 골라주세요.")

        while True:
            print("\n예상치 못한 손실이 발생하면 어떻게 반응하십니까?")
            print("1. 크게 당황함")
            print("2. 약간 불안함")
            print("3. 침착하게 대응함")

            reaction_choice_1 = input("번호를 입력하세요 (1, 2, 3 중에서 하나 골라주세요): ")
            if reaction_choice_1 in ['1', '2', '3']:
                selections.append(reaction_choice_1)
                break
            else:
                print("잘못된 입력입니다. 1, 2, 3 중에서 하나 골라주세요.")

        while True:
            print("\n투자 기간은 얼마나 고려하십니까?")
            print("1. 1년 이하")
            print("2. 1~3년")
            print("3. 3년 이상")

            investment_period_choice = input("번호를 입력하세요 (1, 2, 3 중에서 하나 골라주세요): ")
            if investment_period_choice in ['1', '2', '3']:
                selections.append(investment_period_choice)
                break
            else:
                print("잘못된 입력입니다. 1, 2, 3 중에서 하나 골라주세요.")

        while True:
            print("\n리스크와 수익 중 어느 것을 더 중시하십니까?")
            print("1. 리스크 최소화")
            print("2. 리스크와 수익화 균형")
            print("3. 수익 극대화")

            risk_reward_choice = input("번호를 입력하세요 (1, 2, 3 중에서 하나 골라주세요): ")
            if risk_reward_choice in ['1', '2', '3']:
                selections.append(risk_reward_choice)
                break
            else:
                print("잘못된 입력입니다. 1, 2, 3 중에서 하나 골라주세요.")

        while True:
            print("\n목표하는 연간 수익률은?")
            print("1. 5% 이하")
            print("2. 5~10% 이하")
            print("3. 10% 이상")

            annual_return_choice = input("번호를 입력하세요 (1, 2, 3 중에서 하나 골라주세요): ")
            if annual_return_choice in ['1', '2', '3']:
                selections.append(annual_return_choice)
                break
            else:
                print("잘못된 입력입니다. 1, 2, 3 중에서 하나 골라주세요.")

        # 선택한 번호들의 빈도 수를 계산
        count_1 = selections.count('1')
        count_2 = selections.count('2')
        count_3 = selections.count('3')

        if count_1 > count_2 and count_1 > count_3:
            result = "안정형 : 최소한의 위험을 선호하며 주로 안정적인 수익을 추구하는 투자자입니다."
        elif count_2 > count_1 and count_2 > count_3:
            result = "중립형 : 적당한 수준의 위험을 수용하면서도 균형 잡힌 수익을 기대합니다."
        else:
            result = "공격형 : 높은 성장 잠재력과 수익을 목표로 하며 상당한 위험을 감수할 준비가 되어 있습니다."

        print(f"\n당신은 {result}")

    elif choice == '2':
        # '2'를 선택했을 때는 아무 행동도 하지 않음
        pass
    else:
        print("잘못된 입력입니다. 1 또는 2를 입력해 주세요.")

# 함수 호출
ask_investment_experience()
