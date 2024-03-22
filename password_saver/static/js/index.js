
function generateStrongPassword(length = 15) {
    const charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+";
    let password = "";

    // Generate the base password without requirements
    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * charset.length);
        password += charset[randomIndex];
    }

    // Ensure the password contains at least one uppercase letter
    if (!/[A-Z]/.test(password)) {
        const randomIndex = Math.floor(Math.random() * password.length);
        const uppercaseLetter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        password = password.substring(0, randomIndex) + uppercaseLetter[Math.floor(Math.random() * uppercaseLetter.length)] + password.substring(randomIndex + 1);
    }

    // Ensure the password contains at least one lowercase letter
    if (!/[a-z]/.test(password)) {
        const randomIndex = Math.floor(Math.random() * password.length);
        const lowercaseLetter = "abcdefghijklmnopqrstuvwxyz";
        password = password.substring(0, randomIndex) + lowercaseLetter[Math.floor(Math.random() * lowercaseLetter.length)] + password.substring(randomIndex + 1);
    }

    // Ensure the password contains at least one number
    if (!/\d/.test(password)) {
        const randomIndex = Math.floor(Math.random() * password.length);
        const number = "0123456789";
        password = password.substring(0, randomIndex) + number[Math.floor(Math.random() * number.length)] + password.substring(randomIndex + 1);
    }

    // Ensure the password contains at least one symbol
    if (!/[^A-Za-z0-9]/.test(password)) {
        const randomIndex = Math.floor(Math.random() * password.length);
        const symbol = "!@#$%^&*()-_=+";
        password = password.substring(0, randomIndex) + symbol[Math.floor(Math.random() * symbol.length)] + password.substring(randomIndex + 1);
    }

    return password;
}



// Example usage:
 // Generates a 12-character password
$(".gen").on("click",()=>{
    const password = generateStrongPassword();
    $("#pass").val(password)
    console.log(password)
})
