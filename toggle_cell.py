from IPython.core.display import display, HTML
import openai
from IPython.display import HTML
from IPython.display import display
from ipywidgets import Button
from ipywidgets import widgets

# from IPython.display import clear_output

class tg_c:
    def handler(s):
        def process_input(input_text):
            print("Input:", input_text)

        # Create a text input widget
        input_box = widgets.Text(description="Input:")
        display(input_box)

 
        button = widgets.Button(description="Submit")
        display(button)
        
        # Define the function that will be called when the button is clicked
        def on_button_clicked(b):
            input_text = input_box.value
#             process_input(input_text)
            return input_text
        # Register the button click event handler
        s.input_text=button.on_click(on_button_clicked)
        
    def tg(self):
#         print("starts")
#         self.handler()
#         que=(self.input_text)
        tag = HTML('''<script>
        code_show=true; 
        function code_toggle() {
                $('div.cell.code_cell.rendered.selected div.input').hide();
        } 
        $( document ).ready(code_toggle);
        </script>''')
#         display(tag)
        def my_function():
#             clear_output()
            print("hi")
        def on_button_clicked(b):
            que = input_box.value
            print(que)
            
    #             process_input(input_text)
#                 return input_text
            # Register the button click event handler
#             s.input_text=button.on_click(on_button_clicked)
            print(hint('''
            {}
            '''.format(que)))
#         input_box = widgets.Text(description="Input:")
#         display(input_box)
        input_box = widgets.Textarea(description="Input:")
        input_box.layout.width='auto'
        input_box.layout.max_width='900px'
#         input_box.layout.height = '200px'  # Set the height of the text box
#         input_box.layout.resize = 'horizontal'  # Allow vertical resizing
        display(input_box)
        button = Button(description="hint")
        button.on_click(on_button_clicked)
        def hint(x,auth='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'):
            openai.api_key=auth
            text=f'''{x} just give me steps or algorithm not code for this please'''
            d={'role':'user',"content":text}
            responses=[]
            op=openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[d])
            for i in op['choices']:
            # print(i.keys(),'a')
              if i['finish_reason']=='stop':
                responses.append(i['message']['content'])
                output=responses[0]
            if len(output)<10:
                return 'something went wrong i am not able to get this please retry question'
            else:
                 return output.replace('<code>','').replace('</code>','').strip(' ')
        display(button)
