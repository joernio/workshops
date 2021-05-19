@main def execute(graph: String) = {
    open(graph)
    println("Finding possible buffer overflows")
        def src = cpg.call("malloc").where(_.argument(1).isCallTo(Operators.addition)).l
        cpg.call("memcpy").where { call => 
        call.argument(1)
            .reachableBy(src)
    }.code.l
}

