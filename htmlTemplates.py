
import base64

# Function to get base64 string of an image
def get_image_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Assuming you have 'user_avatar.png' and 'bot_avatar.png' in the same directory as your script
user_image_base64 = get_image_base64("/home/mzkhan/Desktop/llm_project/final_multi_pdf_chatbot/image/human_avatar.png")
bot_image_base64 = get_image_base64("/home/mzkhan/Desktop/llm_project/final_multi_pdf_chatbot/image/bot_image.png")
#aws_image_base64 = get_image_base64("/home/mzkhan/Desktop/llm_project/final_multi_pdf_chatbot/image/aws_image.png")


css = '''
<style>
.chat-message {
    width: 110%;
    margin: auto; /* Center the chat messages */
    padding: 1.5rem; 
    border-radius: 0.5rem; 
    margin-bottom: 1rem; 
    display: flex ; 
    font-size: 1.2rem; 
    align-items: center;
}

h1 {
    text-align: center;
}

.header-title {
  text-align: center;
  font-size: 2.5rem; /* Adjust this value to the size you want */
}


.header-title {
  text-align: center;
  font-size: 2.5rem; /* Adjust this value to the size you want */
  display: flex;
  justify-content: center; /* This ensures the content is centered within the div */
  align-items: center; /* This vertically aligns the content in the middle if the div has a specific height */
}


.header-title img {
    margin-right: 10px; /* Adds a bit of margin to the right of the image */
}


/* To increase the font size of the text above the text box */
.big-text {
    font-size: 2em; /* Change this value as desired */
}


.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #2b313e
}
.chat-message .avatar {
  width: 10%;
}
.chat-message .avatar img {
  max-width: 60px;
  max-height: 60px;
  border-radius: 20%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = f'''
<div class="chat-message bot">
    <div class="avatar">
        <img src="data:image/png;base64,{bot_image_base64}">
    </div>
    <div class="message">{{{{MSG}}}}</div>
</div>
'''

user_template = f'''
<div class="chat-message user">
    <div class="avatar">
        <img src="data:image/png;base64,{user_image_base64}">
    </div>    
    <div class="message">{{{{MSG}}}}</div>
</div>
'''
