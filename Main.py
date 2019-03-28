import json

from CustomException import QuestionPaperCanNotBeGenerated
from QuestionServices import QuestionServices


class Main:

    fileUrl = "questions.txt"
    test_case_url = "test_case.txt"

    service_object = QuestionServices(fileUrl)
    service_object.populate_question_store()

    f = open(test_case_url, 'r')

    for line in f.readlines():
        print("Generating Question Paper for Configuration: " + line)

        configuration = json.loads(line)

        try:
            paper = service_object.get_question_paper(configuration)
            print(paper)
        except QuestionPaperCanNotBeGenerated:
            print('Paper can not be generated for provided configuration')
        print("")
