
function toggleMenu() {
    const menu = document.getElementById("mobileMenu");
    if (menu) {
        menu.classList.toggle("hidden");
    }
}



document.addEventListener("DOMContentLoaded", () => {
    const flashes = document.querySelectorAll(".flash");
    flashes.forEach((flash, index) => {
        flash.style.animationDelay = `${index * 0.15}s`;
        flash.classList.add("flash-show");

        // Remover automaticamente após 5 segundos
        setTimeout(() => {
            flash.classList.add("flash-hide");
        }, 5000);
    });
});



function validateBid(form) {
    const currentPrice = parseFloat(form.current_price.value);
    const bidAmount = parseFloat(form.amount.value);

    if (isNaN(bidAmount) || bidAmount <= 0) {
        showPopup("Digite um valor válido!", "danger");
        return false;
    }

    if (bidAmount <= currentPrice) {
        showPopup("Seu lance deve ser maior que o lance atual!", "danger");
        return false;
    }

    showPopup("Lance enviado!", "success");
    return true;
}



function showPopup(message, type = "info") {
    const popup = document.createElement("div");
    popup.classList.add("popup", `popup-${type}`);
    popup.textContent = message;

    document.body.appendChild(popup);

    setTimeout(() => popup.classList.add("popup-show"), 10);

    setTimeout(() => popup.classList.add("popup-hide"), 3000);

    setTimeout(() => popup.remove(), 3500);
}



document.addEventListener("DOMContentLoaded", () => {
    const cards = document.querySelectorAll(".auction-card");

    cards.forEach(card => {
        card.addEventListener("mouseenter", () => {
            card.style.transform = "translateY(-6px) scale(1.02)";
            card.style.boxShadow = "0 0 25px rgba(79, 124, 255, 0.4)";
        });

        card.addEventListener("mouseleave", () => {
            card.style.transform = "";
            card.style.boxShadow = "";
        });
    });
});



function confirmEndAuction(url) {
    const confirmBox = confirm("Tem certeza que deseja ENCERRAR este leilão?");
    if (confirmBox) {
        window.location.href = url;
    }
}



document.addEventListener("DOMContentLoaded", () => {
    const inputs = document.querySelectorAll("input, textarea");

    inputs.forEach(input => {
        input.addEventListener("focus", () => {
            input.style.boxShadow = "0 0 10px rgba(79,124,255,0.6)";
        });

        input.addEventListener("blur", () => {
            input.style.boxShadow = "";
        });
    });
});



document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll(".btn");

    buttons.forEach(btn => {
        btn.addEventListener("mousedown", () => {
            btn.style.transform = "scale(0.95)";
        });

        btn.addEventListener("mouseup", () => {
            btn.style.transform = "scale(1)";
        });
    });
});



document.querySelectorAll("a").forEach(link => {
    link.addEventListener("click", (event) => {
        if (link.classList.contains("nav-btn") || link.classList.contains("btn")) {
            link.style.opacity = "0.6";
            setTimeout(() => link.style.opacity = "1", 150);
        }
    });
});
