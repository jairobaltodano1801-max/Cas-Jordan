from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():

    destacados = [
        {
            "nombre": "MacBook Air M2",
            "precio": "S/. 5,990",
            "precio_num": 5990,
            "badge": "🔥 Más Vendido",
            "imagen": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=400&q=80"
        },
        {
            "nombre": "iPhone 15 Pro",
            "precio": "S/. 4,200",
            "precio_num": 4200,
            "badge": "⭐ Nuevo",
            "imagen": "https://images.unsplash.com/photo-1695048133142-1a20484d2569?w=400&q=80"
        },
        {
            "nombre": "Samsung 4K 55\"",
            "precio": "S/. 2,800",
            "precio_num": 2800,
            "badge": "💥 Oferta",
            "imagen": "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=400&q=80"
        }
    ]

    productos = [
        {
            "nombre": "Laptop HP Pavilion 15",
            "categoria": "Laptops",
            "categoria_key": "laptops",
            "descripcion": "Intel Core i5, 16GB RAM, 512GB SSD, pantalla Full HD.",
            "precio": "S/. 2,999",
            "precio_num": 2999,
            "imagen": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=400&q=80"
        },
        {
            "nombre": "Laptop Gamer ASUS ROG",
            "categoria": "Laptops",
            "categoria_key": "laptops",
            "descripcion": "Ryzen 7, RTX 4060, 32GB RAM, 1TB SSD, 144Hz.",
            "precio": "S/. 5,499",
            "precio_num": 5499,
            "imagen": "https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=400&q=80"
        },
        {
            "nombre": "MacBook Pro M3",
            "categoria": "Laptops",
            "categoria_key": "laptops",
            "descripcion": "Chip M3, 18GB RAM unificada, 512GB SSD, Liquid Retina.",
            "precio": "S/. 8,990",
            "precio_num": 8990,
            "imagen": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=400&q=80"
        },
        {
            "nombre": "Samsung Galaxy S24",
            "categoria": "Celulares",
            "categoria_key": "celulares",
            "descripcion": "6.2\", Exynos 2400, 256GB, cámara 50MP con IA.",
            "precio": "S/. 3,299",
            "precio_num": 3299,
            "imagen": "https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=400&q=80"
        },
        {
            "nombre": "iPhone 15 128GB",
            "categoria": "Celulares",
            "categoria_key": "celulares",
            "descripcion": "Chip A16, Dynamic Island, USB-C, cámara 48MP.",
            "precio": "S/. 3,799",
            "precio_num": 3799,
            "imagen": "https://images.unsplash.com/photo-1695048133142-1a20484d2569?w=400&q=80"
        },
        {
            "nombre": "Xiaomi Redmi Note 13",
            "categoria": "Celulares",
            "categoria_key": "celulares",
            "descripcion": "6.67\" AMOLED, 108MP, 5000mAh, carga 33W.",
            "precio": "S/. 899",
            "precio_num": 899,
            "imagen": "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=400&q=80"
        },
        {
            "nombre": "Cargador 65W GaN",
            "categoria": "Accesorios",
            "categoria_key": "accesorios",
            "descripcion": "Carga rápida universal, compatible con laptops y celulares.",
            "precio": "S/. 89",
            "precio_num": 89,
            "imagen": "https://images.unsplash.com/photo-1583863788434-e58a36330cf0?w=400&q=80"
        },
        {
            "nombre": "Auriculares Sony WH-1000XM5",
            "categoria": "Accesorios",
            "categoria_key": "accesorios",
            "descripcion": "Cancelación de ruido líder, 30h batería, Bluetooth 5.2.",
            "precio": "S/. 1,299",
            "precio_num": 1299,
            "imagen": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400&q=80"
        },
        {
            "nombre": "Mouse Logitech MX Master 3",
            "categoria": "Accesorios",
            "categoria_key": "accesorios",
            "descripcion": "Ergonómico, scroll electromagnético, 70 días batería.",
            "precio": "S/. 399",
            "precio_num": 399,
            "imagen": "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=400&q=80"
        }
    ]

    servicios = [
        {
            "nombre": "Diagnóstico y Optimización",
            "descripcion": "Análisis completo del sistema, limpieza de virus, optimización de rendimiento y actualización de drivers.",
            "icono": "fas fa-search"
        },
        {
            "nombre": "Reparación de Laptops",
            "descripcion": "Cambio de pantallas, teclados, puertos, mantenimiento interno, pasta térmica y microsoldadura.",
            "icono": "fas fa-laptop-medical"
        },
        {
            "nombre": "Recuperación de Datos",
            "descripcion": "Recuperación de archivos perdidos por formateo, virus o daño físico en discos duros y USB.",
            "icono": "fas fa-database"
        }
    ]

    return render_template('index.html',
                           productos=productos,
                           servicios=servicios,
                           destacados=destacados)

if __name__ == '__main__':
    app.run(debug=True, port=5000)