import sqlite3
conn = sqlite3.connect('gramatas.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS gramata (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nosaukums TEXT NOT NULL,
autors TEXT NOT NULL,
lapas INTEGER NOT NULL
)
''')
ieraksti = [
('Zvejnieka dēls', 'Vilhelms Purvītis', 320),
('Mērnieku laiki', 'Kaudzītes brāļi', 450),
('Bille', 'Vizma Belševica', 275),
('Purva bridējs', 'Rūdolfs Blaumanis', 180),
('Dvēseļu putenis', 'Aleksandrs Grīns', 500),
('Ceplis', 'Pāvils Rozītis', 330),
('Nāves ēnā', 'Rūdolfs Blaumanis', 120)
]
cursor.executemany('''
INSERT INTO gramata (nosaukums, autors, lapas)
VALUES (?, ?, ?)
''', ieraksti)
conn.commit()
cursor.execute('''
SELECT nosaukums, autors, lapas
FROM gramata
ORDER BY lapas DESC
LIMIT 1
''')
visbiezaka = cursor.fetchone()
print("Visbiežākā grāmata:")
print(f"Nosaukums: {visbiezaka[0]}, Autors: {visbiezaka[1]}, Lapas: {visbiezaka[2]}")
conn.close()

