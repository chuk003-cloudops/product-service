# Product Service

The Product Service is a Rust/Warp API that returns the product catalog from /products. For Lab 2 it runs on its own Azure VM and reads its listening port from environment configuration.

## Configuration

The service reads PORT from the process environment or an optional local .env file. The default is 3030; .env.example documents this non-secret setting. Keep .env out of Git.

PORT=3030

## Install and run

On the product-service VM, install Rust, Cargo, and build-essential. From this repository root, run cargo build --locked and cargo run --locked. The service listens on all IPv4 interfaces at port 3030 by default. Its NSG should allow TCP 3030 only from the laptop public IP.

## Verify

From another terminal on the VM, run curl -i http://localhost:3030/products. Expect HTTP 200 and three products with IDs, names, and prices. From the laptop browser, use http://PRODUCT_SERVICE_VM_PUBLIC_IP:3030/products with the actual public IP substituted.
