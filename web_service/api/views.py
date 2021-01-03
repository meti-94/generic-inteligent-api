from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import InputJsonSerializer, OutputJsonSerializer
from .engine import engine


# eng = engine()




@api_view(['POST'])
# @renderer_classes([JSONRenderer])
def main(request):
	_response = {'confidence':100, 'label':'positive'}
	print(OutputJsonSerializer(_response).validated_data)
	Response(OutputJsonSerializer(_response).validated_data)


	# serialized_request = InputJsonSerializer(data=request.data)
	# if serialized_request.is_valid():
	# 	request_data = serialized_request.validated_data
	# 	probs = eng.predict(request_data)
	# 	if max(probs)-min(probs)>0.33:
	# 		conf = round(max(probs)*100)
	# 		label = probs.index(max(probs))
	# 		print(label, conf)
	# 		if label==1:
	# 			_response = {'confidence':conf, 'label':'positive'}
	# 			Response(OutputJsonSerializer(_response).data)
	# 		else:
	# 			_response = {'confidence':conf, 'label':'negative'}
	# 			Response(OutputJsonSerializer(_response).data)

	# else:
	# 	return Response(serialized_request.errors)
	

	
	
