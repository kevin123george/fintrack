package com.astra.fintrack.controller;

import com.astra.fintrack.dtos.PortfolioStats;
import com.astra.fintrack.dtos.StockRequest;
import com.astra.fintrack.model.StockHolding;
import com.astra.fintrack.services.StockService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/stocks")
public class StockController {

    private final StockService service;

    public StockController(StockService service) {
        this.service = service;
    }

    @PostMapping
    public ResponseEntity<StockHolding> addStock(@RequestBody StockRequest req) {
        return ResponseEntity.ok(service.addStock(req));
    }

    @GetMapping
    public ResponseEntity<List<StockHolding>> getAllStocks() {
        return ResponseEntity.ok(service.getAllStocks());
    }

    @PutMapping("/{id}")
    public ResponseEntity<StockHolding> updatePrice(@PathVariable Long id,
                                                    @RequestParam double currentPrice) {
        return ResponseEntity.ok(service.updatePrice(id, currentPrice));
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteStock(@PathVariable Long id) {
        service.deleteStock(id);
        return ResponseEntity.noContent().build();
    }

    @GetMapping("/stats")
    public ResponseEntity<PortfolioStats> getStats() {
        return ResponseEntity.ok(service.getPortfolioStats());
    }
}
