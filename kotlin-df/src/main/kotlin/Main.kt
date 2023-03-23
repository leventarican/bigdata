import org.jetbrains.kotlinx.dataframe.DataFrame
import org.jetbrains.kotlinx.dataframe.api.*
import org.jetbrains.kotlinx.dataframe.io.read

private const val CSV_PATH = "./TR-maaslar-2023.csv"

fun debug() {
    val df = DataFrame.read(CSV_PATH)
    df.print(rowsLimit = 3)

    df.columnNames().joinToString {
        "$it |"
    }.also {
        println(it)
    }

    // data schema
    df.schema().print()

    val a = df
        .groupBy(df.columns()[2])
        .sortBy{ df.columns()[0] }
        .aggregate {
            count() into "count"
            mean() into "mean"
        }
    a.print()

    val b = df
        .groupBy(df.columns()[2])
        .sortBy{ df.columns()[0] }.concat()
    b.print(rowsLimit = 3)

    val c = df.convert {
        columns()[3]
    }.with {cell ->
        cell as String
        cell.replace("Yıl", "").trim()
    }
    c.print(rowsLimit = 3)
}

fun main(args: Array<String>) {
    println("schemaless")
    debug()
}