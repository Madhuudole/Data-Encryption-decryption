# 🔐 Data Encryption Techniques

This project explores classical and modern symmetric encryption algorithms including **DES**, **Triple DES**, and **AES**, with detailed breakdowns, numerical examples, and performance evaluations.

---

## 📚 Table of Contents

- [Introduction](#introduction)
- [Encryption Algorithms](#encryption-algorithms)
  - [DES](#des)
  - [Triple DES (3DES)](#triple-des-3des)
  - [AES](#aes)
- [Data Types Encrypted](#data-types-encrypted)
- [Performance Metrics](#performance-metrics)
- [Comparative Analysis](#comparative-analysis)
- [Applications](#applications)
- [Conclusion](#conclusion)
- [References](#references)

---

## 📖 Introduction

**Data encryption** ensures data confidentiality by converting plaintext into unreadable ciphertext using cryptographic keys. Only authorized users with decryption keys can reverse the process. This project demonstrates and compares popular symmetric encryption methods.

---

## 🔐 Encryption Algorithms

### DES (Data Encryption Standard)

- Block cipher: 64-bit blocks
- Key: 56-bit
- Operations: 16 rounds of permutations, substitutions, and XORs
- Vulnerability: Susceptible to brute-force attacks due to short key size

### Triple DES (3DES)

- Applies DES three times with three keys
- Key length: 168-bit effective
- Enhanced security, but slower

### AES (Advanced Encryption Standard)

- Block size: 128 bits
- Key sizes: 128, 192, 256 bits
- Highly secure, efficient, and widely used
- Resistant to brute-force and side-channel attacks

---

## 🖼️ Data Types Encrypted

This project includes theoretical encryption methods for:

- Text data
- Images
- Video content

Algorithms used:
- DES
- Triple DES
- AES

---

## ⏱️ Performance Metrics

| Metric             | Description                              |
|--------------------|------------------------------------------|
| Encryption Time    | Time to convert plaintext to ciphertext  |
| Decryption Time    | Time to revert ciphertext to plaintext   |
| Key Strength       | Resistance to brute-force attacks        |
| Memory Usage       | RAM needed for encryption/decryption     |
| Energy Consumption | Power required for operations            |

---

## 📊 Comparative Analysis

| Attribute       | DES       | Triple DES | AES         |
|------------------|-----------|-------------|-------------|
| Key Length       | 56 bits   | 168 bits    | 128–256 bits |
| Rounds           | 16        | 48 (3×16)   | 10–14        |
| Security         | Low       | Moderate    | High         |
| Speed            | Fast      | Slower      | Fast         |
| Energy Efficiency| Medium    | Low         | High         |

---

## 📌 Applications

- 🔐 Securing sensitive data (e.g. medical, financial)
- 💬 Encrypted communications
- 💽 Disk and file encryption
- 📡 Wireless/mobile security

---

## ✅ Conclusion

Each algorithm has trade-offs. DES is outdated and insecure. Triple DES improves security but is resource-heavy. AES offers the best balance of security, speed, and efficiency, making it the industry standard today.

---

## 📚 References

1. [Performance Evaluation for DES and AES Algorithms - IEEE](https://ieeexplore.ieee.org/document/9012536)
2. [Image Data Encryption Using DES Method - IEEE](https://ieeexplore.ieee.org/document/9609738)


![image](https://github.com/user-attachments/assets/187a77fb-9d6b-4cdb-af2d-1baa309a8a8a)


