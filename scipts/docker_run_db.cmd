@echo off

docker run --name hw10-postgres -p 5432:5432 --env-file ../.env -d postgres


                    

