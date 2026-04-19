from ragas import evaluate

def run_eval(dataset):
    result = evaluate(
        dataset,
        metrics=["faithfulness", "answer_relevancy"]
    )

    print(result)
