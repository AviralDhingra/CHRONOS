from langchain.agents import create_pandas_dataframe_agent
from langchain.llms import OpenAI
import pandas as pd
import os


def loadDF(fileName):
    # can load from xlsx and power BI live data as well
    df = pd.read_csv(fileName)
    return df


def qna(df, query):
    agent = create_pandas_dataframe_agent(OpenAI(
        temperature=0, openai_api_key="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"), df, verbose=False)
    ans = agent.run(query)
    return ans


if __name__ == "__main__":
    os.system("clear")
    print("Press Ctrl-C to quit.\n")
    status = True
    while status:
        try:
            query = input("Question : ")
            res = qna(loadDF('test_data.csv'), query)
            print(f"Answer: {res}")
            print("\n")
        except KeyboardInterrupt:
            print(f"\n[+] Keyboard Interupt\n[+] Exiting")
            status = False
            break
