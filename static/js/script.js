// ===== CARRITO =====
let carrito = [];
let total = 0;

function toggleCarrito() {
    const panel = document.getElementById('carritoPanel');
    const overlay = document.getElementById('overlayCarrito');
    panel.classList.toggle('abierto');
    overlay.classList.toggle('activo');
}

function agregarCarrito(nombre, precio, precioNum) {
    carrito.push({ nombre, precio, precioNum });
    total += precioNum;
    actualizarCarrito();

    // Animación de confirmación en el botón
    const btn = event.target.closest('button');
    const original = btn.innerHTML;
    btn.innerHTML = '<i class="fas fa-check"></i> ¡Agregado!';
    btn.style.background = '#25d366';
    setTimeout(() => {
        btn.innerHTML = original;
        btn.style.background = '';
    }, 1500);
}

function actualizarCarrito() {
    const items = document.getElementById('carritoItems');
    const contador = document.getElementById('contador-carrito');
    const totalEl = document.getElementById('totalCarrito');

    contador.textContent = carrito.length;
    totalEl.textContent = 'S/. ' + total.toLocaleString();

    if (carrito.length === 0) {
        items.innerHTML = '<p class="carrito-vacio">Tu carrito está vacío</p>';
        return;
    }

    items.innerHTML = carrito.map((item, i) => `
        <div class="carrito-item">
            <div>
                <strong style="font-size:13px;">${item.nombre}</strong><br>
                <span style="color:#0066ff;font-weight:700;">${item.precio}</span>
            </div>
            <button onclick="eliminarItem(${i})"><i class="fas fa-trash"></i></button>
        </div>
    `).join('');
}

function eliminarItem(index) {
    total -= carrito[index].precioNum;
    carrito.splice(index, 1);
    actualizarCarrito();
}

// ===== MODAL PAGO =====
function mostrarFormularioPago() {
    if (carrito.length === 0) {
        alert('Tu carrito está vacío');
        return;
    }

    const resumen = document.getElementById('resumenCompra');
    resumen.innerHTML = `
        <strong>Resumen de tu pedido:</strong><br><br>
        ${carrito.map(i => `• ${i.nombre} — ${i.precio}`).join('<br>')}
        <br><br><strong>Total: S/. ${total.toLocaleString()}</strong>
    `;

    document.getElementById('modalPago').classList.add('activo');
    document.getElementById('modalOverlay').classList.add('activo');
    toggleCarrito();
}

function confirmarCompra() {
    alert('✅ ¡Compra realizada con éxito! Nos contactaremos contigo pronto.');
    carrito = [];
    total = 0;
    actualizarCarrito();
    cerrarModal('modalPago');
}

// ===== MODAL CITA =====
function mostrarFormularioCita(servicio) {
    document.getElementById('servicio-seleccionado').textContent = '🔧 ' + servicio;
    document.getElementById('modalCita').classList.add('activo');
    document.getElementById('modalOverlay').classList.add('activo');
}

function confirmarCita() {
    alert('✅ ¡Cita agendada! Te contactaremos para confirmar tu cita técnica.');
    cerrarModal('modalCita');
}

// ===== CERRAR MODALES =====
function cerrarModal(id) {
    document.getElementById(id).classList.remove('activo');
    document.getElementById('modalOverlay').classList.remove('activo');
}

function cerrarTodosModales() {
    document.getElementById('modalPago').classList.remove('activo');
    document.getElementById('modalCita').classList.remove('activo');
    document.getElementById('modalOverlay').classList.remove('activo');
}

// ===== FILTROS CATÁLOGO =====
function filtrar(categoria, btn) {
    document.querySelectorAll('.filtro').forEach(b => b.classList.remove('activo'));
    btn.classList.add('activo');

    document.querySelectorAll('#grid-productos .card').forEach(card => {
        if (categoria === 'todos' || card.dataset.categoria === categoria) {
            card.style.display = 'flex';
        } else {
            card.style.display = 'none';
        }
    });
}