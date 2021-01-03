from transformers import BertTokenizerFast, BertForSequenceClassification
from transformers import pipeline
from .serializers import InputJsonSerializer

# config = AutoConfig.from_pretrained("/content/drive/MyDrive/new_parsebert/config.json", local_files_only=True)
# tokenizer = AutoTokenizer.from_pretrained("HooshvareLab/bert-fa-base-uncased")
# model = BertForSequenceClassification.from_pretrained('/content/drive/MyDrive/new_parsebert/')

class engine:
	def __init__(self):
		self.model = BertForSequenceClassification.from_pretrained('api/files/sentiment_pipeline/')
		self.tokenizer = BertTokenizerFast.from_pretrained('api/files/sentiment_pipeline/')
		self.pipeline = pipeline("sentiment-analysis",return_all_scores=True,  
								 model=self.model, tokenizer=self.tokenizer)


	def predict(self, _input):
		text = _input['docBody']
		return [item['score'] for item in self.pipeline(text)[0]]

if __name__=='__main__':
	eng = engine()
	