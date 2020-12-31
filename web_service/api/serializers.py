from rest_framework import serializers

class InputJsonSerializer(serializers.Serializer):
	lang = serializers.CharField(max_length=2)
	docType = serializers.IntegerField(max_value=None, min_value=0)
    docTitle = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    docBody = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    docSummary = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    docTags = serializers.ListField(child=str, allow_empty=True, min_length=None, max_length=None)
    
