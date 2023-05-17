from IPython.display import clear_output
from IPython.core.display import display, HTML
import openai
from IPython.display import HTML
from IPython.display import display
from ipywidgets import Button
from ipywidgets import widgets
from simple_colors import * 
# from IPython.display import clear_output
q=1
c=0
class tg_c:
    def tg(self):
        global c
        tag = HTML('''<script>
        code_show=true; 
        function code_toggle() {
                $('div.cell.code_cell.rendered.selected div.input').hide();
        } 
        $( document ).ready(code_toggle);
        </script>''')
        if c==0:
            input_box1 = widgets.Textarea(description="Enter key:")
            input_box1.layout.width='800px'
            output=widgets.Output()
            def on_button_clicked1(b):
                global q
                global auth
                auth = input_box1.value
                # print(auth,'inp1')
                def on_button_clicked(b):
                    global q
                    que = input_box.value
                    # print(que,'b1')
                    # print(auth,'inp2')
                    if auth!='':
                        print(f'{green("Q")} {q} :{green(que)}')
                        text=f'''{que} just give me steps or algorithm not code for this and only answer my question if it is related to python programming else write \"not related to programming.\" '''
                        print(f'A {q} :{hint(text)}\n\n')
                        input_box.value=''
                    else:
                            print('please restart kernel and input key')      
                    q+=1              
                def on_button_clicked_eval(b):
                    global q
                    x = input_box.value
                    # print(que,'b_eval')
                    # print(auth,'inp2')
                    if auth!='':
                        print(f'{green("Q")} {q}:{green(x)}')
                        # print(que)
                        que=f"""Evaluate below given code on scale of 5 and how you evaluate code in short and explain me the code as well ```{x}``` also can you provide explaination in points so it's easy for me to read"""
                        text=(hint(que))
                        print(f'A {q} :{text}\n\n')
                        input_box.value=''
                    else:
                            print('please restart kernel and input key')
                    q+=1
                input_box = widgets.Textarea(description="Input:")
                input_box.layout.width='auto'
                input_box.layout.max_width='900px'
                display(input_box)
                button = Button(description="hint")
                button.on_click(on_button_clicked)
                button_eval = Button(description="Evaluate and explain code")
                button_eval.on_click(on_button_clicked_eval)
                button_layout = widgets.Layout(display='flex', flex_flow='row', justify_content='space-between', width='700px')
                # Arrange the buttons with spacing using the layout
                button_container = widgets.HBox([button, widgets.HTML('&nbsp;'), button_eval], layout=button_layout)
                display(button_container)
            display(input_box1)
            button1 = widgets.Button(description="Submit")
            display(button1)
            button1.on_click(on_button_clicked1)
        else:
              def on_button_clicked(b):
                    global q
                    x = input_box.value
                    if auth!='':
                        que=f'''{x} just give me steps or algorithm not code for this and only answer my question if it is related to python programming else write \"not related to programming.\" '''
                        print(f'{green("Q")} {q}:{green(x)}')
                        # print(que)
                        text=(hint(que))
                        print(f'A {q} :{text}\n\n')
                        input_box.value=''
                    else:
                            print('please restart kernel and input key')
                    q+=1                  
              def on_button_clicked_eval(b):
                    global q
                    x = input_box.value
                    if auth!='':
                        que=f"""Evaluate below given code on scale of 5 and how you evaluate code in short and explain me the code as well ```{x}``` also can you provide explaination in points so it's easy for me to read"""
                        print(f'{green("Q")}{q}:{green(x)}')
                        text=(hint(que))
                        print(f'A {q} :{text}\n\n')
                        input_box.value=''
                    else:
                            print('please restart kernel and input key')
                    q+=1  
              input_box = widgets.Textarea(description="Input:")
              input_box.layout.width='auto'
              input_box.layout.max_width='900px'
              display(input_box)
              button = Button(description="hint")
              button.on_click(on_button_clicked)
              button_eval = Button(description="Evaluate and explain code")
              button_eval.on_click(on_button_clicked_eval)
              button_layout = widgets.Layout(display='flex', flex_flow='row', justify_content='space-between', width='700px')
              # Arrange the buttons with spacing using the layout
              button_container = widgets.HBox([button, widgets.HTML('&nbsp;'),  button_eval], layout=button_layout)
              display(button_container)
        def hint(text):
            system_message = {
            'role': 'system',
            'content': '''You are chatting with a programming expert. Please ask me programming-related questions for other questions i will just give \"not related to programming.\" '''}
            # clear_output()
            openai.api_key=auth.strip()
            d={'role':'user',"content":text,}
            responses=[]
            op=openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[system_message,d])
            for i in op['choices']:
            # print(i.keys(),'a')
              if i['finish_reason']=='stop':
                responses.append(i['message']['content'])
                output=responses[0]
            if len(output)<10:
                return 'something went wrong i am not able to get this please retry question'
            else:
                 return output.replace('<code>','').replace('</code>','').strip(' ')
        # print("X-----")
        c=c+1                
