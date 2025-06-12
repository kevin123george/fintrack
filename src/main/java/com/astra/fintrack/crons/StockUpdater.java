package com.astra.fintrack.crons;

import com.astra.fintrack.services.StockService;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

@Component
public class StockUpdater {

    private final PolygonStockService polygonStockService;

    private final StockService stockService;
    public StockUpdater(PolygonStockService service, StockService stockService) {
        this.polygonStockService = service;
        this.stockService = stockService;
    }

    @Scheduled(fixedDelay = 10000)
    public void updateStock() {
            stockService.updateHoldingCurrentPrice();
    }
}
