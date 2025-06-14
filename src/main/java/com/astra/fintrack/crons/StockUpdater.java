package com.astra.fintrack.crons;

import com.astra.fintrack.services.StockService;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

@Component
public class StockUpdater {

    private final StockService stockService;
    public StockUpdater(StockService stockService) {
        this.stockService = stockService;
    }

    @Scheduled(fixedDelay = 60000)
    public void updateStock() {
            stockService.updateHoldingCurrentPrice();
    }
}


//watch list -- nike salando apple benz bmw adiddas amundi