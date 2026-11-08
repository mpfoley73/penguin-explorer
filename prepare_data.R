con <- DBI::dbConnect(duckdb::duckdb(dbdir = "my-db.duckdb"))

DBI::dbWriteTable(con, "penguins", palmerpenguins::penguins)

DBI::dbDisconnect(con)

# # Checks
# con <- DBI::dbConnect(duckdb::duckdb(dbdir = "my-db.duckdb"))
# DBI::dbListTables(con)
# DBI::dbGetQuery(con, "SELECT COUNT(*) AS n FROM penguins")
# DBI::dbDisconnect(con)
