package com.astra.fintrack.repos;

import com.astra.fintrack.model.StockHolding;
import com.astra.fintrack.model.StockHoldingHistory;
import org.springframework.data.jpa.repository.JpaRepository;

public interface StockHoldingHistoryRepository extends JpaRepository<StockHoldingHistory, Long> {
}
