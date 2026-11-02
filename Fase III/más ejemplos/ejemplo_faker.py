from faker import Faker

fake = Faker("es_MX")  # locale en español/México

# Generar un "usuario falso" para pruebas
print(fake.name())           # Sofía Torres Herrera
print(fake.email())          # sofía.torres@example.mx
print(fake.ipv4_private())   # 192.168.4.37
print(fake.user_agent())     # Mozilla/5.0 (Windows NT...
print(fake.password(length=16, special_chars=True))

# Caso práctico: poblar una BD de prueba
usuarios = [
    {"nombre": fake.name(), "ip": fake.ipv4(), "mac": fake.mac_address()}
    for _ in range(5)
]
for u in usuarios:
    print(u)
