# from email import message
# from socket import timeout
# from turtle import title
# import pyjokes
# from plyer import notification

# if __name__ == "__main__":
#     joke = pyjokes.get_jokes('en','all')
#     notification.notify(
#         title = "Jokes Time!!!!",
#         message = "".join(joke),
#         app_icon = "./logo.ico",
#         timeout = 10
#     )
# import pyttsx3
# engine = pyttsx3.init()
# engine.setProperty('rate', 150)
# engine.say("Hello sir how are you??")
# engine.runAndWait()
def removeLoop(self, head):
        
        slow = head
        fast = head
        flag = 0
       
       #This chechking for loop in the linked list 
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                flag = 1
                break
        
        #If there is a loop in linked list    
        if flag == 1:    
            prev = None
            meet = slow
            slow = head
            while slow != meet:
                prev = meet
                slow = slow.next
                meet = meet.next
            prev.next = None
            return head
            
        # If there is no loop
        else:
            return head