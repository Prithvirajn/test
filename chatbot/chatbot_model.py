from transformers import AutoModelForCausalLM, AutoTokenizer

class ChatbotModel:
    def __init__(self, model_name="microsoft/DialGPT-medium"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def get_response(self, user_input):
        inputs = self.tokenizer.encode(user_input + self.tokenizer.eos_token, return_tensors="pt")
        outputs = self.model.generate(inputs, max_length=1000, pad_token_id=self.tokenizer.eos_token_id)
        response = self.tokenizer.decode(outputs[:, inputs.shape[-1]:][0], skip_special_tokens=True)
        return response
