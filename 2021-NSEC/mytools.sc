// 1. Possible Buffer Overflows

def buffer_overflows(cpg : io.shiftleft.codepropertygraph.Cpg) = {
    def src = cpg.call("malloc").where(_.argument(1).isCallTo(Operators.addition)).l
    cpg.call("memcpy").where { call => 
    call.argument(1)
        .reachableBy(src)
    }.code.l
}


