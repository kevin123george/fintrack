package com.astra.fintrack.services;

import com.astra.fintrack.dtos.PortfolioStats;
import com.astra.fintrack.dtos.StockRequest;
import com.astra.fintrack.model.StockHolding;
import com.astra.fintrack.repos.StockRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class StockService {

    private final StockRepository repo;

    public StockService(StockRepository repo) {
        this.repo = repo;
    }

    public List<StockHolding> getAllStocks() {
        return repo.findAll();
    }

    public StockHolding addStock(StockRequest req) {
        StockHolding stock = new StockHolding();
        stock.setSymbol(req.symbol);
        stock.setQuantity(req.quantity);
        stock.setBuyPrice(req.buyPrice);
        stock.setBuyDate(req.buyDate);
        stock.setCurrentPrice(req.currentPrice);
        return repo.save(stock);
    }

    public StockHolding updatePrice(Long id, double newPrice) {
        StockHolding stock = repo.findById(id)
                .orElseThrow(() -> new RuntimeException("Stock not found"));
        stock.setCurrentPrice(newPrice);
        return repo.save(stock);
    }

    public void deleteStock(Long id) {
        repo.deleteById(id);
    }

    public PortfolioStats getPortfolioStats() {
        List<StockHolding> holdings = repo.findAll();
        double invested = 0;
        double current = 0;

        for (StockHolding s : holdings) {
            invested += s.getQuantity() * s.getBuyPrice();
            current += s.getQuantity() * s.getCurrentPrice();
        }

        return new PortfolioStats(invested, current, current - invested);
    }
}
