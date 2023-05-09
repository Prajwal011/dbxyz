from IPython.core.display import display, HTML
import openai
from IPython.display import HTML
from IPython.display import display
from ipywidgets import Button
from ipywidgets import widgets

# from IPython.display import clear_output
c=0
# auth=''
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
            input_box1.layout.width='auto'
            output=widgets.Output()
            def on_button_clicked1(b):
                global auth
                auth = input_box1.value
                # print(auth,'inp1')
                def on_button_clicked(b):
                    que = input_box.value
                    # print(auth,'inp2')
                    if auth!='':
                        print(hint(que))
                    else:
                            print('please restart kernel and input key')                    
                input_box = widgets.Textarea(description="Input:")
                input_box.layout.width='auto'
                input_box.layout.max_width='900px'
                display(input_box)
                button = Button(description="hint")
                button.on_click(on_button_clicked)
                display(button)
                # button1.on_click(on_button_clicked1)
                # return auth
            display(input_box1)
            button1 = widgets.Button(description="Submit")
            display(button1)
            button1.on_click(on_button_clicked1)
        else:
            def on_button_clicked(b):
                    que = input_box.value
                    # print(auth)
                    print(hint(que))
            input_box = widgets.Textarea(description="Question:")
            input_box.layout.width='auto'
            input_box.layout.max_width='900px'
            display(input_box)
            button = Button(description="hint")
            button.on_click(on_button_clicked)
            display(button)
        # print(auth,'inp3')
        def hint(x):
            openai.api_key=auth.strip()
            text=f'''please only answer my question if it is related to programming {x} just give me steps or algorithm not code for this please'''
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
        c=c+1        
        
#     def tg(self):
#         global auth
#         global c
# #         print(c)            
# #         print("starts")
# #         self.handler()
# #         que=(self.input_text)
#         tag = HTML('''<script>
#         code_show=true; 
#         function code_toggle() {
#                 $('div.cell.code_cell.rendered.selected div.input').hide();
#         } 
#         $( document ).ready(code_toggle);
#         </script>''')
# #         display(tag)
#         if c==0:

#             input_box1 = widgets.Textarea(description="Enter key:")
#             input_box1.layout.width='auto'
#     #         output = widgets.Output()
#     #         # Define an async function to handle the events
#     #         async def handle_input(change):
#     #             # Check if the first input box has a value
#     #             if text_box1.value:
#     #                 # Display the second input box and output widget
#     #                 display(text_box2, output)

#     #         # Register the event handler for the first input box
#     #         text_box1.observe(handle_input, 'value')

#     #         # Display the first input box
#     #         display(input_box1)

#             output=widgets.Output()
#     #         def handle_inp(chg):
#     #             if input_box1.value:
#                     # Define the function that will be called when the button is clicked
#             def on_button_clicked1(b):
#                 auth = input_box1.value
#     #             process_input(input_text)
#     #                 return input_text
#     #             self.auth=button1.on_click(on_button_clicked1)
#                 def on_button_clicked(b):
#                     que = input_box.value
#                     print(auth)
#                     if auth.strip()!='':
# #                         print(auth)
#                         print(hint(que,auth))
#                     else:
#                             print('please restart kernel and input key')
#                     return auth
                    
# #                         print(hint(''' {}'''.format(que)))
#                 input_box = widgets.Textarea(description="Input:")
#                 input_box.layout.width='auto'
#                 input_box.layout.max_width='900px'
#         #         input_box.layout.height = '200px'  # Set the height of the text box
#         #         input_box.layout.resize = 'horizontal'  # Allow vertical resizing
#                 display(input_box)
#                 button = Button(description="hint")
#                 auth=button.on_click(on_button_clicked)
#                 display(button)
#                 button1.on_click(on_button_clicked1)
#                 return auth
#     #         input_box1.observe(handle_inp,'value')
#             display(input_box1)
#     #         display(input_box1)
#             button1 = widgets.Button(description="Submit")
#             display(button1)
#             self.auth=button1.on_click(on_button_clicked1)
#         else:
#             def on_button_clicked(b):
#                     que = input_box.value
#                     print(self.auth)
#                     print(hint(que,self.auth))
#             input_box = widgets.Textarea(description="Question:")
#             input_box.layout.width='auto'
#             input_box.layout.max_width='900px'
#             display(input_box)
#             button = Button(description="hint")
#             button.on_click(on_button_clicked)
#             display(button)
#         c=c+1
#         def hint(x,auth):
# #             if self.auth=='' or self.auth==None or len(self.auth)<2:
# #                 self.auth='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'
#             print(auth)
#             openai.api_key=auth.strip()
# #             print(auth,x,len(x))
#             text=f'''{x} just give me steps or algorithm not code for this please'''
#             d={'role':'user',"content":text}
#             responses=[]
#             op=openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[d])
#             for i in op['choices']:
#             # print(i.keys(),'a')
#               if i['finish_reason']=='stop':
#                 responses.append(i['message']['content'])
#                 output=responses[0]
#             if len(output)<10:
#                 return 'something went wrong i am not able to get this please retry question'
#             else:
#                  return output.replace('<code>','').replace('</code>','').strip(' ')
# # 
