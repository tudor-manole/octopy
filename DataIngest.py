#!/usr/bin/env python

# TM

from neo4j.v1 import GraphDatabase

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "octopy"))

with open('fakedataset.csv', 'r', encoding = 'utf-8') as f:
    with driver.session() as session:
        with session.begin_transaction() as tx:
            for line in f:
                ip, port, date = line.split(',')
                _ = tx.run("""MERGE (port:Port { value: {port} })
                            MERGE (ip:IP { value: {ip} })
                            MERGE (ip) -[sent:SENT]-> (packet:Packet) -[on:ON]-> (port)""", ip=ip, port=999)


# notes for future:
# MATCH (peter { name: 'Peter' }) RETURN peter
# MERGE (peter { name: 'Peter' }) ON MATCH SET peter += { hungry: TRUE , position: 'Entrepreneur' }
# MATCH (peter { name: 'Peter' }) RETURN peter
# # added two new properties here
# MERGE (peter { name: 'Peter' }) ON MATCH SET peter += { hungry: FALSE , position: 'Entrepreneur' }
# MATCH (peter { name: 'Peter' }) RETURN peter
