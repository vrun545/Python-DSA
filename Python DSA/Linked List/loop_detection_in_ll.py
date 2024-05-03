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