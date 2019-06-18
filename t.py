from mindmeld.components import QuestionAnswerer

qa = QuestionAnswerer('.')
qa.load_kb('placement','companies','./data/companies.json')

companies = qa.get(index='companies')

for i in companies:
   print(i)
