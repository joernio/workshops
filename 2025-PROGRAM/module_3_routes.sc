
       @main def execute(path: String) = {
            println("\n#####  Generating CPG...\n")
            importCode(path)
            println("\n#####  Extracting Routes...\n")
            cpg.call
              .where(_.code(".*route.*(GET|POST).*"))
              .where(_.name("route")).argument
              .where(_.argumentIndex(1))
              .code.toJsonPretty
         }

