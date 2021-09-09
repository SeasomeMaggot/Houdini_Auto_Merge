selected = hou.selectedNodes()
tupleLen = len(selected)

if tupleLen is 0:

    raise hou.Error("Select the fvcking nodes before merging!!!")
    print("先TM选节点再合并!!!")
    
else:
  
    mergeNode = selected[0].node("..").createNode("merge", "auto_merge")
    mergeNode.moveToGoodPosition()
    
    for n in range(tupleLen):
        
        hou.node(mergeNode.path()).setInput(n, hou.node(selected[n].path()))
