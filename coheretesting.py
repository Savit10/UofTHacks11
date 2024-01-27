import cohere 
co = cohere.Client('JC3UOkxURSbxNHDxonzLvCtDuekGMAqovUXneDwU') 
response = co.chat(
  model='46564f19-ad66-4af6-b167-4c60a0f50010-ft',
  message='Where do you live?') 
print(response.text)