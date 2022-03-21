/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
 const removeNthFromEnd = function(head, n) {
    
    const reversed = (current) => {
        if(current === null) return current
        if(current.next === null) return current
        
        let nextNode = current.next
        current.next = null
        let rest = reversed(nextNode)
        nextNode.next = current
        return rest
    }
    
    const deleteAtIndex = (index) => {

       head = reversed(head);
       let current = head,    
        count = 1,
        previos;

        if(index <= 0){
            return head;
        }
     
      if(index === 1){
            head = current.next;
            current.next = null;
            return head;
        }

        while(count < index){
            previos = current;
            current = current.next;
            count++;
        }

        let nextNode = current.next;
        current.next = null;
        previos.next = nextNode;
        return head

    }
    
    return reversed(deleteAtIndex(n))
  
    
};