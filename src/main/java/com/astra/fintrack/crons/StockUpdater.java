package com.astra.fintrack.crons;

import com.astra.fintrack.model.StockWatch;
import com.astra.fintrack.repos.StockWatchRepository;
import com.astra.fintrack.services.StockService;
import com.astra.fintrack.services.StockWatchService;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Service;

@Component
public class StockUpdater {

    private final StockService stockService;

    private final StockWatchRepository stockWatchRepository;

    private final StockWatchService stockWatchService;
    public StockUpdater(StockService stockService, StockWatchRepository stockWatchRepository, StockWatchService stockWatchService) {
        this.stockService = stockService;
        this.stockWatchRepository = stockWatchRepository;
        this.stockWatchService = stockWatchService;
    }



    @Scheduled(fixedDelay = 10000)
    public void updateStock() {
            stockService.updateHoldingCurrentPrice();
    }


    @Scheduled(fixedDelay = 10000)
    public void updatedWatcher() {
        stockWatchRepository.findDistinctStockSymbols().forEach(stockWatchService::recordCurrentPrice);
    }
}


//watch list -- nike salando apple benz bmw adiddas amundi